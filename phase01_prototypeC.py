# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Written by : Jordan Beaubien
# ----------------------
# This program demonstrates a current working prototype of Rose Coloured Waveform.
# This program takes an audio file and transforms the audio frequencies along the
#   pink noise power spectrum. In this demonstration the transformation uses a 
#   the reciprocal of the square root of the frequency as the scalar instead of the
#   true pink noise ratio of 1/frequency. This is to maintain a more listenable
#   experience.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import librosa              # pip install librosa
import numpy as np          # pip install numpy
from scipy import signal    # pip install scipy
import soundfile            # pip install soundfile

# sample audio file, works with various audio formats.
# filename = "./NightmaresOnWax_YouWish_plain.aiff"
filename = "./NightmaresOnWax_YouWish_plain.mp3"

# load audio data to program.
audio_fileIN = soundfile.SoundFile(filename, mode='r')
audio_data_frameByCH = audio_fileIN.read(always_2d=True)

# audio data has the inverse dimensions that the fourier function expects as input, must reshape.
""" Reshape 'F', column-major mode, changes the array from (samples, channels) to
    (channels, samples) where each sample has the left and right sample per homogenous cell. """
audio_data_CHbyFrame = audio_data_frameByCH.reshape((2, audio_data_frameByCH.size // 2), order='F')

# windowing settings for the short-time fourier transform.
""" n_fft is the length of the windowed signal. (ensure is a power of 2 for efficient fourier transform)
     256 : low frequency distortion
     512 : heavier centre, more gain in lower frequencies
    1024 : maintain apparent centre
    2048 : more contrast in width of sound field. """
n_fft = 512 # default = 2048
""" hop_length : n_fft - hop_length = overlap relative to each window """
hop_length = n_fft // 2

# "in order to enable inversion of an STFT via the inverse STFT (iSTFT), it is sufficient
# that the signal windowing obeys the constrains. This ensures that every point in the 
# input data is equally weighted, thereby avoiding aliasing and allowing full reconstruction."
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.check_COLA.html 
""" Check whether the Constant Overlap Add Constraint is met. """
assert signal.check_COLA('hann', n_fft, hop_length) == True

""" Perform Short-Time Fourier Transform (STFT) """
audio_stft = librosa.stft(audio_data_CHbyFrame, n_fft=n_fft, hop_length=hop_length)

# the data represents magnitude of frequencies at each frame. 
# librosa.fft_frequencies gathers which specific frequencies are being represented.
""" Get frequencies for chosen stft window. """
lib_freqs = librosa.fft_frequencies(sr=audio_fileIN.samplerate, n_fft=n_fft) 

""" 1/freq ratio for each frequency follow pink noise power spectrum.
    1/sqrt(f) sounds more pink. Not true pink. 
    1/cbrt(f) less pink.                  """
lib_freqs[0] = 1.0 # avoid divide by zero
reciprocal_freqs = np.divide(1, np.sqrt(lib_freqs)) # pink-ish, freq = 1/sqrt(freq)
reciprocal_freqs *= (np.cbrt(993) // 3) # attempt at maintaining volume after transform

# multiply the magnitudes of a frequency for every frame according to the
# prescribed ratio for the weighting of that frequency along the spectrum.
""" Perform transformation with respect to reciprocal of frequency. """
for i in range(len(audio_stft[0])):
  audio_stft[0][i] *= reciprocal_freqs[i] # left channel
  audio_stft[1][i] *= reciprocal_freqs[i] # right channel

""" Invert the stft transformation. """
audio_istft = librosa.istft(audio_stft, n_fft=n_fft, hop_length=hop_length)

# re-reshape array dimensions for proper write to file.
""" Reshape into original shape array before flatten. """
audio_transformed = audio_istft.reshape((audio_istft.size // 2, 2), order='F')

""" Write transformed audio to a new file. """
# with soundfile.SoundFile('NightmaresOnWax_YouWish_pinkish.aiff', 
with soundfile.SoundFile('NightmaresOnWax_YouWish_pinkish.mp3', 
                         mode='w', samplerate=audio_fileIN.samplerate, 
                         channels=audio_fileIN.channels, format=audio_fileIN.format) as f:
  f.write(audio_transformed)

# finished with opened audio file
audio_fileIN.close()