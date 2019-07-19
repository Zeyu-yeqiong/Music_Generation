# Unconditional music generation

Music generation system

## Preparation

### Training data
Using processing data to generate training data

A default data has been put in data folder

### Requirement

  ```sh
  pip install pretty_midi
  pip install pypianoroll
  pip install librosa
  pip install pydub
  pip install tensorflow   (>10.0.0)

  FluidSynth
  ```

## Training model

```sh
python src/train.py --exp_dir exp/my_experiment --params exp/my_experiment/params.yaml --config exp/my_experiment/config.yaml --gpu 0
```
**Data shape must equal to the setting in config.yaml and deep neural network**

A default model has been put in exp folder


## Output
### Using interpolation method
```sh
./scripts/run_interpolation.sh "./exp/my_experiment/" "0"
```
### or
```sh
./scripts/run_inference.sh "./exp/my_experiment/" "0"
```
Bernoulli sampling has been deleted

## SF2
SoundFont is a file format for sample based instrument sounds.
5 default sf2 file has been put in sf2lib folder, and it will influence the music quality.

## Sample Result
Sample result can be found in sample folder, and their label is 'Epic'.
