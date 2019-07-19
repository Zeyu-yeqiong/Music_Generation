# Data Processing

Convert midi file to training data.
## Prerequisites
Midi file can be download from [Free Midi](https://freemidi.org/) or [Lakh MIDI Dataset](https://colinraffel.com/projects/lmd/)

Midi label can be found from [Million song dataset.lastfm](http://millionsongdataset.com/lastfm/)

  ```sh
  pip install joblib
  pip install pretty_midi
  pip install pypianoroll
  pip install librosa
  pip install pydub
  ```

## Convert midi file to array

Use converter.py
Parallel kernal number can be modified in config.py


## Select track

Use merger_5.py
Default track is Piano,Guitar,Base,String,Ensemble.
[Midi Program Detail](https://www.midi.org/specifications-old/item/gm-level-1-sound-set)

## Combine

-Unconditional training
use combine_unconditional.py

-Conditional training
### Extract BPM information
Use multitrack ,convert npz file to midi
Convert midi to wav file,use BPM.py to calculate midi BPM and save as BPM_label.npy

### Get the training data
Use combine_conditional.py
