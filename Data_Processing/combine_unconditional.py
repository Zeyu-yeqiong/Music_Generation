
import os
from pypianoroll import Multitrack
import numpy as np
import gc
 



path ="D:/MusicMidi/labeltest"
i=0
BEAT_RESOLUTION=12
N_TRACKS=4
results = []
for files in os.listdir(path):
    NpzName=path+'/'+files
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
    print(pianoroll.shape)
    if pianoroll.shape[0] < 4 * 4 * BEAT_RESOLUTION:
        print('music too short')
        continue

    # Keep only the mid-range pitches
        
    pianoroll = pianoroll[:, 24:108]
    # Reshape and get the phrase pianorolls
    pianoroll = pianoroll.reshape(-1,4 * BEAT_RESOLUTION, 84, N_TRACKS)
    if pianoroll.shape[0]%4!=0:
        pianoroll=pianoroll[:-(pianoroll.shape[0]%4)]
    print(pianoroll.shape)
    pianoroll = pianoroll.reshape(-1,2,4 * BEAT_RESOLUTION, 84, N_TRACKS)
    pianorolls=np.concatenate(
        [pianoroll[:-3], pianoroll[1:-2], pianoroll[2:-1], pianoroll[3:]], 1)

    # remove unqualified phase
    low_index=[]
    rank=0
    print(pianorolls.shape)
    if pianorolls.shape[0]<3:
        continue
    else:
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
    print(pianorolls.shape)
    print('-------------')
    pianorolls=np.delete(pianorolls,low_index,axis=0)
    print(pianorolls.shape)
    results.append(pianorolls)


    i+=1
    print(files+'Success    '+str(i))

result = np.concatenate(results, 0)

np.savez_compressed(
    'temp.npz', nonzero=np.array(result.nonzero()),
    shape=result.shape)
print(result.shape)


