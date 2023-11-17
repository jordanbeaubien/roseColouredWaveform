from scipy.io import wavfile
from scipy import fft, signal
import matplotlib.pyplot as plt
import numpy as np
import librosa
import soundfile as sf



# hold string of path to audio file. Must be a .wav
# filename = "/Users/jb/Desktop/Fall2023/MUSIC_645/Final_Project/DonCaballero_Punkgasm_DirtyLooks-001.wav"

# generate two identical copies of sample data for audio file
# samplerate_original, data_original = wavfile.read(filename)
# samplerate_fft, data_fft = wavfile.read(filename)

# data.shape[1] holds the number of channels in the audio file
# channels = data_original.shape[1]

# data.shape[0] holds the total amount of samples for the entire audio file
# total samples divided by the samplerate gives duration of audio file in seconds
# length = data_original.shape[0] / samplerate_fft
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
# fft_original = fft.fft(data_original)
# magnitude_spectrum_wav = np.abs(fft_original)

# #plot magnitude spectrum
# plt.figure(figsize=(18, 5))

# frequency = np.linspace(0,samplerate_original, len(magnitude_spectrum_wav))
# num_frequency_bins = int(len(frequency) * 0.00005) # f_ratio=1

# plt.plot(frequency[:num_frequency_bins], magnitude_spectrum_wav[:num_frequency_bins])
# plt.xlabel("Frequency (Hz)")
# plt.title("Magnitude Spectrum")
# plt.show()


# def display_spectrogram(data:np.ndarray, sample_rate:int) -> None:
def display_spectrogram(filename:str) -> None:
# needs to be split into two functions
# this currently transforms using STFT and generates spectrogram
  
  data, sample_rate = librosa.load(filename, sr=None, mono=False) # sr=None preserves native sample rate of file
  dataFile = sf.SoundFile(filename, mode='r')
  data_SF = dataFile.read(always_2d=True)

  print(len(data_SF) / sample_rate)

  # with sf.SoundFile('testWriteSF.wav', 'w', 44100, 2, 'PCM_24') as f:
  #   f.write(data_SF)

  dataFile.close()

  # sf.write('testWriteSF.wav', dataSF, sample_rateSF)
  # print(data)


  """ Duration of audio file in seconds. """
  # print(data.shape[0] / sample_rate)
  
  # modifier = 1/8 # less precise
  # modifier = 4
  FRAME_SIZE = 2048 # default sample rate for librosa, well adapted for music signals
  HOP_SIZE = 512 # default is win_length // 4

  # S_scale = librosa.stft(scale, n_fft=FRAME_SIZE, hop_length=HOP_SIZE)
  data_stft = librosa.stft(data, n_fft=FRAME_SIZE, hop_length=HOP_SIZE)
  # print(data_stft.size)

  # plot_samples_waveform(dataFile, dataFile.samplerate, "librosaLoad", "blue", "purple")

  # dataABS_stft = np.abs(data_stft) ** 2
  # dataLOG_stft = librosa.power_to_db(dataABS_stft)
  # plt.figure(figsize=(16, 5))

  # librosa.display.specshow(dataABS_stft, sr=sample_rate, hop_length=HOP_SIZE, x_axis="time", y_axis="linear")
  # librosa.display.specshow(dataLOG_stft, sr=sample_rate, hop_length=HOP_SIZE, x_axis="time", y_axis="log")
  # plt.colorbar(format="%+2.f")
  # plt.show()



def process_audio_file(filename:str) -> tuple[int, np.ndarray]:
  '''
  Reads data from a .wav audio file and returns it's samplerate and
  a numpy array of the samples.

  filename : path to the audio file 
  '''
  samplerate, data = wavfile.read(filename)
  return samplerate, data


def plot_samples_waveform(data:np.ndarray, sample_rate:int, title:str, leftCH_color:str, rightCH_color:str) -> None:
  '''
  Creates a Matplotlib graph for amplitude over time for the waveform.

  data : sample data read from .wav audio file
  sample_rate : the sample rate of the sample data
  title : graph title
  leftCH_color : graph line color for left channel
  rightCH_color : graph line color for right channel
  '''
  length = data.shape[0] / sample_rate
  time = np.linspace(0., length, data.shape[1])
  plt.plot(time, data[0], label="Left Channel", color=leftCH_color)
  # plt.plot(time, data[:, 0], label="Left Channel", color=leftCH_color)
  plt.plot(time, data[1], label="Right Channel", color=rightCH_color)
  # plt.plot(time, data[:, 1], label="Right Channel", color=rightCH_color)
  plt.legend(loc='center')
  plt.title(title)
  plt.xlabel("Time [seconds]")
  plt.ylabel("Amplitude")
  plt.show()


def display_time_details(data:np.ndarray, sample_rate:int, filename:str) -> None:
  '''
  Print basic .wav file information to the terminal.
  
  data : sample data read from .wav audio file
  sample_rate : the sample rate of the sample data
  filename : path to the audio file
  '''
  print('\n# # # # # #')
  print(f'# FILENAME: {filename}')
  print(f'# CHANNELS: {data.shape[1]}ch')
  print(f'# SAMP/SEC: {sample_rate:,}KHz')
  print(f'# TOTSAMPL: {len(data[:, 0]):,} per channel') 
  print(f'# DURATION: {data.shape[0] / sample_rate}s')    # data.shape[0] is total samples for entire audio file
  print('# # # # # #')


if __name__ == "__main__":
  
  # get sample data for .wav audio file
  filename = "/Users/jb/Desktop/Fall2023/MUSIC_645/Final_Project/DonCaballero_Punkgasm_DirtyLooks-001.wav"
  # samplerate_original, data_original = process_audio_file(filename)
  
  # show basic details and amplitude waveform for audio file
  #display_time_details(data_original, samplerate_original, filename)
  #plot_samples_waveform(data_original, samplerate_original, "original", '0.8', '0.5')
  # plot_samples_waveform(fft_original, samplerate_original, "original", '0.8', '0.5')

  # display_spectrogram(data_original, samplerate_original)
  display_spectrogram(filename)
  
  pass # if all main code is commented out