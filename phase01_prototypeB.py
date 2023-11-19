# import matplotlib.pyplot as plt
from scipy import signal
import numpy as np
import librosa
import soundfile

# filename = "/Users/jb/Desktop/Fall2023/MUSIC_645/Final_Project/DonCaballero_Punkgasm_DirtyLooks-001.wav"
filename = "./../AgainstAllLogic_Alarm_plain.mp3"

audio_fileIN = soundfile.SoundFile(filename, mode='r')
audio_data_frameByCH = audio_fileIN.read(always_2d=True)

""" flatten 'F' converts to 1D, column-major mode
  we transformed a shape (samples, 2) where each sample has the left and right
  sample per homogenous cell, into an array of all left and then all right samples.
  The array will always be an even number in size. """
""" This is not what affects the apparent centre of the sound field. """
audio_data_CHbyFrame = audio_data_frameByCH.reshape((2, audio_data_frameByCH.size // 2), order='F')

""" n_fft : length of the windowed signal. (ensure is a power of 2 for efficient fourier transform)
     256 : low frequency distortion
     512 : heavier centre, more gain in lower frequencies
    1024 : maintain apparent centre
    2048 : more contrast in width of sound field. """
n_fft = 1024 # default = 2048, old value is 16384 which is what caused odd behavior

""" hop_length : n_fft - hop_length = overlap relative to each window """
hop_length = n_fft // 2 # old value was // 2

""" Check whether the Constant Overlap Add Constraint is met. """
assert signal.check_COLA('hann', n_fft, hop_length) == True

""" Perform Short-Time Fourier Transform (STFT) """
audio_stft = librosa.stft(audio_data_CHbyFrame, n_fft=n_fft, hop_length=hop_length)

""" Get frequencies for chosen stft window. """
lib_freqs = librosa.fft_frequencies(sr=audio_fileIN.samplerate, n_fft=n_fft) 

""" 1/freq ratio for each frequency 
    1/sqrt(f) sounds more pink. Not true pink. 
    1/cbrt(f) sounds pink-ish.                  """
lib_freqs[0] = 1.0 # avoid divide by zero
reciprocal_freqs = np.divide(1, np.sqrt(lib_freqs)) # pink-ish
# reciprocal_freqs = np.divide(1, np.cbrt(lib_freqs))
# reciprocal_freqs *= (993 // 5)
reciprocal_freqs *= (np.sqrt(993) // 2)
# reciprocal_freqs *= (np.sqrt(993) // 5)

""" Example setting a low frequency cutoff for applied reciprocal ratio. """
# lpf = 500
# for i in range(len(lib_freqs)):
#   if lib_freqs[i] < lpf:
#     reciprocal_freqs[i] = 1.0

""" Perform transformation with respect to reciprocal of frequency. """
""" This is not what affects the apparent centre of the sound field. """
for i in range(len(audio_stft[0])):
  audio_stft[0][i] *= reciprocal_freqs[i]
  audio_stft[1][i] *= reciprocal_freqs[i]  

""" invert the stft transformation """
audio_istft = librosa.istft(audio_stft, n_fft=n_fft, hop_length=hop_length)

""" Reshape into original shape array before flatten """
""" This is not what affects the apparent centre of the sound field. """
audio_transformed = audio_istft.reshape((audio_istft.size // 2, 2), order='F')

# with soundfile.SoundFile('testProtoB.wav', mode='w', samplerate=44100, channels=2, format=audio_fileIN.format) as f:
with soundfile.SoundFile('AgainstAllLogic_Alarm_pinkIsh.mp3', mode='w', samplerate=audio_fileIN.samplerate, channels=audio_fileIN.channels, format=audio_fileIN.format) as f:
  f.write(audio_transformed)

audio_fileIN.close()