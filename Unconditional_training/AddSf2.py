import os
import wave
from pypianoroll import Multitrack
from midi2audio import FluidSynth


count=0
sf2name='C:/Users/Ma Zeyu/Downloads/musegan-master/sf2lib/Nice-Keys-Ultimate-V2.3.sf2'

for filename in os.listdir('D:/MusicMidi/4_4Npz5'):
    filepath='D:/MusicMidi/4_4Npz5/'+filename
    fs=FluidSynth()
    fs.__init__(sf2name)
    pcmname='./test/'+filename[:filename.index('.')]+'.pcm'
    fs.midi_to_audio(filepath,pcmname)
    with open(pcmname, 'rb') as pcmfile:
        pcmdata = pcmfile.read()
    wav_name=pcmname[:-4]+'.wav'
    with wave.open(wav_name, 'wb') as wavfile:
        wavfile.setparams((2, 2, 44100, 0, 'NONE', 'NONE'))
        wavfile.writeframes(pcmdata)
    k+=1
    if k>5:
        break