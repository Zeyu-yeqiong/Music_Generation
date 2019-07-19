import os
import wave
from pypianoroll import Multitrack
from midi2audio import FluidSynth



for sf2 in os.listdir('./sf2lib'):
    sf2name='C:/Users/Ma Zeyu/Downloads/musegan-master/sf2lib/'+sf2
    m = Multitrack('b23eb7f99a9d4575c29ff7aaa5fbcb16.npz')
    m.write('./test/'+sf2+'.midi')
    fs=FluidSynth()
    fs.__init__(sf2name)
    print('success')
    fs.midi_to_audio('./test/'+sf2+'.midi','./test/'+sf2+'.pcm')
    print('1success')
    with open('./test/'+sf2+'.pcm', 'rb') as pcmfile:
        pcmdata = pcmfile.read()
    wav_name='./test/'+sf2[:-4]+'.wav'
    print('2success')
    with wave.open(wav_name, 'wb') as wavfile:
        wavfile.setparams((2, 2, 44100, 0, 'NONE', 'NONE'))
        wavfile.writeframes(pcmdata)
    print('3success')