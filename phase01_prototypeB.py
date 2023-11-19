import matplotlib.pyplot as plt
from scipy import signal
import numpy as np
import librosa
import soundfile

filename = "/Users/jb/Desktop/Fall2023/MUSIC_645/Final_Project/DonCaballero_Punkgasm_DirtyLooks-001.wav"

audio_fileIN = soundfile.SoundFile(filename, mode='r')
audio_data_frameByCH = audio_fileIN.read(frames=4321792, always_2d=True)

""" flatten 'F' converts to 1D, column-major mode
  we transformed a shape (samples, 2) where each sample has the left and right
  sample per homogenous cell, into an array of all left and then all right samples.
  The array will always be an even number in size. """
audio_data_CHbyFrame = audio_data_frameByCH.reshape((2, audio_data_frameByCH.size // 2), order='F')

""" n_fft : length of the windowed signal. """
n_fft = 2048 # default = 2048, old value is 16384 which is what caused odd behavior
hop_length = n_fft // 2 # old value was // 2

""" Check whether the Constant Overlap Add Constraint is met. """
assert signal.check_COLA('hann', n_fft, hop_length) == True

""" Perform Short-Time Fourier Transform (STFT) """
audio_stft = librosa.stft(audio_data_CHbyFrame, n_fft=n_fft, hop_length=hop_length)

""" Get frequencies for chosen stft window. """
lib_freqs = librosa.fft_frequencies(sr=audio_fileIN.samplerate, n_fft=n_fft) 

""" 1/freq ratio for each frequency 
    1/sqrt(f) sounds more pink. Not true pink. """
lib_freqs[0] = 1.0 # avoid divide by zero
reciprocal_freqs = np.divide(1, np.sqrt(lib_freqs))
# reciprocal_freqs *= (993 // 5)
reciprocal_freqs *= (np.sqrt(993) // 2)

""" Example setting a low frequency for applied reciprocal ratio. """
# lpf = 500
# for i in range(len(lib_freqs)):
#   if lib_freqs[i] < lpf:
#     reciprocal_freqs[i] = 1.0

""" Perform transformation with respect to reciprocal of frequency. """
for i in range(len(audio_stft[0])):
  audio_stft[0][i] *= reciprocal_freqs[i]
  audio_stft[1][i] *= reciprocal_freqs[i]  

""" invert the stft transformation """
audio_istft = librosa.istft(audio_stft, n_fft=n_fft, hop_length=hop_length)

""" Reshape into original shape array before flatten """
audio_transformed = audio_istft.reshape((audio_istft.size // 2, 2), order='F')

with soundfile.SoundFile('testProtoB.wav', 'w', 44100, 2, 'PCM_24') as f:
  f.write(audio_transformed)

audio_fileIN.close()