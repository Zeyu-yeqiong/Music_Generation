import numpy as np
from pydub import AudioSegment
import os
import csv
import librosa



res=[]

k=0
for foldername in os.listdir('D:/workoutput'):
    for musicname in os.listdir('D:/workoutput/'+foldername):

        song_dir= 'D:/workoutput/'+foldername+'/'+musicname
        y, sr = librosa.load(song_dir, mono=True, duration=10)
        bpm = librosa.beat.tempo(y=y, sr=sr)
        
        name=foldername+musicname[:-4]
        print(name,bpm)
        res.append([name,int(bpm+0.5)])
    k=k+1
    if k%100==0:
        result=np.concatenate(res,0)
        np.save('BPM_label'+str(k)+'.npy',result)
        res=[]
result=np.concatenate(res,0)
np.save('BPM_label'+str(k)+'.npy',result)

               



