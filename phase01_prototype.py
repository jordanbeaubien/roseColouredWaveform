from scipy.io import wavfile
from scipy import fft
import matplotlib.pyplot as plt
import numpy as np

# hold string of path to audio file. Must be a .wav
filename = "/Users/jb/Desktop/Fall2023/MUSIC_645/Final_Project/DonCaballero_Punkgasm_DirtyLooks-001.wav"

# generate two identical copies of sample data for audio file
samplerate_original, data_original = wavfile.read(filename)
samplerate_fft, data_fft = wavfile.read(filename)

# data.shape[1] holds the number of channels in the audio file
channels = data_original.shape[1]

# data.shape[0] holds the total amount of samples for the entire audio file
# total samples divided by the samplerate gives duration of audio file in seconds
length = data_original.shape[0] / samplerate_fft
# print(f'{data_original.shape[0]}samples over {length}seconds')
# print(len(data_original[:, 0]), data_original[:, 0])
# print(len(data_original[:, 1]), data_original[:, 1])

# fft_original = fft.fft(data_original)
# print(type(fft_original))
# print(fft_original[0])

# discard imaginary portion of complex numbers
# magnitude_spectrum_wav = np.abs(fft_original)
# print(magnitude_spectrum_wav[0])


""" plot_magnitude_spectrum : Valerio Velardo Youtube"""
fft_original = fft.fft(data_original)
magnitude_spectrum_wav = np.abs(fft_original)

#plot magnitude spectrum
plt.figure(figsize=(18, 5))

frequency = np.linspace(0,samplerate_original, len(magnitude_spectrum_wav))
num_frequency_bins = int(len(frequency) * 0.00005) # f_ratio=1

plt.plot(frequency[:num_frequency_bins], magnitude_spectrum_wav[:num_frequency_bins])
plt.xlabel("Frequency (Hz)")
plt.title("Magnitude Spectrum")
plt.show()



# Matplotlib amplitude over time for waveform
def plot_samples_waveform(data:np.ndarray, sample_rate:int, title:str, leftCH_color:str, rightCH_color:str) -> None:
  length = data.shape[0] / sample_rate
  time = np.linspace(0., length, data.shape[0])
  plt.plot(time, data[:, 0], label="Left Channel", color=leftCH_color)
  plt.plot(time, data[:, 1], label="Right Channel", color=rightCH_color)
  plt.legend(loc='center')
  plt.title(title)
  plt.xlabel("Time [seconds]")
  plt.ylabel("Amplitude")
  plt.show()

# Print basic .wav file information to the terminal.
def display_time_details(data:np.ndarray, sample_rate:int, filename:str) -> None:
  print('\n# # # # # #')
  print(f'# FILENAME: {filename}')
  print(f'# CHANNELS: {data.shape[1]}ch')
  print(f'# SAMP/SEC: {sample_rate:,}KHz')
  print(f'# TOTSAMPL: {len(data[:, 0]):,} per channel') 
  print(f'# DURATION: {data.shape[0] / sample_rate}s')
  print('# # # # # #')


if __name__ == "__main__":
  #display_time_details(data_original, samplerate_original, filename)
  #plot_samples_waveform(data_original, samplerate_original, "original", '0.8', '0.5')
        # plot_samples_waveform(fft_original, samplerate_original, "original", '0.8', '0.5')
  pass