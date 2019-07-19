
import os
from pypianoroll import Multitrack
import numpy as np
import gc



label=np.load('BPM_label.npy').tolist()
d={}
for k in range(len(label)//2):
    d[label[2*k]]=int(label[2*k+1])
labels=[]
path ="./4_4Npz4"
i=0
BEAT_RESOLUTION=12
N_TRACKS=4
N_BARS=4
results = []
for files in os.listdir(path):
    NpzName=path+'/'+files
    try:
        multitrack= Multitrack(NpzName, beat_resolution=BEAT_RESOLUTION)
    
        # Pad to multtple
        multitrack.pad_to_multiple(4 * BEAT_RESOLUTION)

        # Binarize the pianoroll
        multitrack.binarize()

        # Sort the tracks according to program number
        multitrack.tracks.sort(key=lambda x: x.program)

        # Bring the drum track to the first track
        multitrack.tracks.sort(key=lambda x: ~x.is_drum)

        # Get the stacked pianoroll
        pianoroll = multitrack.get_stacked_pianoroll()
        # Check length
        if pianoroll.shape[0] < N_BARS *4 * 4 * BEAT_RESOLUTION:
            print('music too short ')
            continue

        # Keep only the mid-range pitches
        pianoroll = pianoroll[:, 24:108]
        # Reshape and get the phrase pianorolls
        try:
            pianoroll = pianoroll.reshape(-1,4 * BEAT_RESOLUTION, 84, N_TRACKS)
            if pianoroll.shape[0]%N_BARS != 0 :
                pianoroll=pianoroll[:-(pianoroll.shape[0]%N_BARS)]
            pianorolls = pianoroll.reshape(-1,N_BARS,4 * BEAT_RESOLUTION, 84, N_TRACKS)

            # remove unqualified phase
            label_name,label_list=[],[]
            low_index=[]
            rank=0
            for ii in pianorolls:
                q=0
                for j in ii:
                    for k in j:
                        for l in k:
                            for m in l:
                                if m ==True:
                                    q=q+1

                if q <= 500:
                    low_index.append(rank)
                rank+=1
            tem=[o for o in range(pianorolls.shape[0])]

            print(pianorolls.shape)
            print('-------------')
            pianorolls=np.delete(pianorolls,low_index,axis=0)
            print(pianorolls.shape)

            if pianorolls.shape[0]>1:
                pianorolls=np.concatenate([pianorolls[:-1], pianorolls[1:]],1)
            else:
                continue
            print(pianorolls.shape)
            llist=[]
            # stick a label for every phase
            tem=np.delete(np.array(tem),low_index,axis=0)
            #search bpm information from dic,speed definition can be modified
            Have=True
            for o in range(tem.shape[0]-1):
                if files[:-4]+str(tem[o])+'_'+str(tem[o+1]) in d:
                    m=d[files[:-4]+str(tem[o])+'_'+str(tem[o+1])]
                    if m>123:
                         llist.append([True,False,False])
                    elif m==123:
                         llist.append([False,True,False])
                    elif m<123:
                         llist.append([False,False,True])
                else:
                    Have=False
                    break
            if len(llist)!=pianorolls.shape[0]:
                Have=False
            if not Have:
                print('Not label Error')
                continue

            results.append(pianorolls)
            for k in llist:
                labels.append(k)
            print(len(labels))

        except:
            print(files+'    reshape failed')
            continue
        i+=1
        print(files+'Success!'+str(i))
    except:
        print(files+'  failed')
        continue
label=labels.copy()
labels = np.array(labels)
result = np.concatenate(results, 0)
np.savez_compressed(
    'temp.npz', nonzero=np.array(result.nonzero()),
    shape=result.shape)
print(result.shape)
np.save('label.npy',labels)
print(labels.shape)
