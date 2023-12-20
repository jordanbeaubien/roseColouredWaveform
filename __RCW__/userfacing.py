#import transformation

import librosa              # pip install librosa
import numpy as np          # pip install numpy
from scipy import signal    # pip install scipy
import soundfile            # pip install soundfile        


class rcw_interface:
  '''
  Perform all process and logic for the Rose Coloured Waveform terminal application.
  Include displaying the terminal interface, prompting a user for necessary input and
  transformed input digital audio along a preferred colour noise power spectrum.
  '''
  def __init__(self):
    # file path details (IN & OUT sections)
    self.inFileName = False
    self.outFileName = False
    self.destinationFolderName = False
    self.destinationPath = False

    # rcw transform settings (RCW section)
    self.hiCut = False
    self.loCut = False
    self.colour = False
    self.hasDefault = False

    # sound file details (SND section)
    self.sampleRate = False
    self.channels = False
    self.format = False
    self.soundFile = soundfile.SoundFile
    self.hasSoundFile = False

    # flag to loop process for multiple audio transformations
    self.transforming = True

    # flag to colourize user input or skip and restart
    self.submittable = False

  # print the user interface here
  def displayInterface(self):
    '''
    Display TUI (text-based user interface) within a terminal window.
    '''
    print("\n" * 40)                  # simulate screen refresh with blank lines
    print("  8888888b.   .d8888b.  888       888")
    print("  888   Y88b d88P  Y88b 888   o   888")
    print("  888    888 888    888 888  d8b  888")
    print("  888   d88P 888        888 d888b 888")
    print("  8888888P   888        888d88888b888")
    print("  888 T88b   888    888 88888P Y88888")
    print("  888  T88b  Y88b  d88P 8888P   Y8888")
    print("  888   T88b   Y8888P   888P     Y888")
    print("        -- enter 'q' to quit -- ")
    
    print("\n -------------------------------------")
    ##### IN #####
    ##### IN #####
    if (self.inFileName):             # display user-provided pre-transformation file
      print(" | [✔] | Operand File:   | " + self.inFileName)
    else:
      print(" | [ ] | Operand File:   | (unknown)       ")
    print(" -------------------------------------")
    ##### RCW #####
    ##### RCW #####
    if (self.colour):                 # display noise power spectrum colour setting
      print(" |  R  | Colour Setting: | " + self.colour)
    else:
      print(" |  R  | Colour Setting: | (unknown)       ")
    if (self.hiCut):                  # display user-chosen hi-frequency cutoff of the transformation
      print(" |  C  | Hi-Freq Cut-off | " + str(self.hiCut) + "Hz")
    else:
      print(" |  C  | Hi-Freq Cut-off | (unknown)       ")
    if (self.loCut):                  # display user-chosen lo-frequency cutoff of the transformation
      print(" |  W  | Lo-Freq Cut-off | " + str(self.loCut) + "Hz")
    else : 
      print(" |  W  | Lo-Freq Cut-off | (unknown)       ")
    print(" -------------------------------------")
    ##### SND #####
    ##### SND #####
    if (self.hasSoundFile):           # display file-decoded audio format
      print(" |  S  | AudioFormat:    | " + self.soundFile.format)
    else:
      print(" |  S  | AudioFormat:    | (unknown)")
    if (self.hasSoundFile):           # display file-decoded channel count
      print(" |  N  | Channels:       | " + str(self.soundFile.channels))
    else: 
      print(" |  N  | Channels:       | (unknown)")
    if (self.hasSoundFile):           # display file-decoded sample rate
      print(" |  D  | SampleRate:     | " + str(self.soundFile.samplerate))
    else:
      print(" |  D  | SampleRate:     | (unknown)")
    print(" -------------------------------------")
    ##### GO #####
    ##### GO #####
    if (self.destinationFolderName):  # display folder where the transformed audio file will be written
      print(" |  G  | Destination:    | " + self.destinationFolderName)
    else:
      print(" |  G  | Destination:    | (unknown)       ")
    if (self.outFileName):            # display user-chosen name of file
      print(" |  O  | Resultant File: | " + self.outFileName)
    else: 
      print(" |  O  | Resultant File: | (unknown)       ")
    print(" -------------------------------------")

  def checkSpecialInput(self, input:str):
    '''
    Did the user try to quit the program by entering a designated key?
      >> "q" - to quit
    '''
    input = input.strip().lower()
    if (input == "q"):
      print(" Goodbye ☺")
      exit()

  def getInputFile(self):
    '''
    Prompt the user to provide an absolute or relative path to an audio file.
    Accepted file types vary. https://pysoundfile.readthedocs.io/en/latest/#soundfile.SoundFile 
    '''
    filepathFull = input("\n Enter the the path to your audio file\n ").strip()
    self.checkSpecialInput(filepathFull)
    try:                         # try block in case provided file path is invalid
      filepathSegments = filepathFull.split("/")
      self.inFileName = filepathSegments.pop(-1)
      self.destinationFolderName = filepathSegments[-1] + "/"
      self.destinationPath = "/".join(filepathSegments) + "/"
      self.soundFile = soundfile.SoundFile(filepathFull, mode='r')
      self.hasSoundFile = True   # flag to print out for display of soundfile details 
      self.outFileName = "(unknown)." + str(self.soundFile.format).lower()
    except:
      print("\n [!!] Please enter a valid absolute or relative filepath to the digital sound you want to transform")

  def getOutFileName(self):
    '''
    Prompt the user to provide the exact filename for the transformed audio file.
    Filename does not include path to file or file-type extension.
    These values are derived from the input file path and type.
    '''
    filename = input("\n Enter the name of the output ." + str(self.soundFile.format).lower() + " file. (without file format extension)\n ").strip()
    self.checkSpecialInput(filename)
    self.outFileName = filename + "." + str(self.soundFile.format).lower()
    self.destinationPath += self.outFileName

  def setDefault(self):
    '''
    Prompt the user to use or not use provided default parameters.
    Defaults:
      - colour: "Pink" for pink noise spectrum scalar transformation of original soundfile
      - hiCut & loCut: False to disengage these parameters
    '''
    validInput = False 
    while not validInput:
      decision = input("\n Would you like to use the default values? (Y/N): ").lower().strip()
      self.checkSpecialInput(decision)
      if decision == "y":
        validInput = True
        self.hasDefault = True
      elif decision == "n":
        validInput = True
        self.hasDefault = False
      else:
        print(" Please input 'Y' for Yes or 'N' for No")
    if self.hasDefault:
      self.hiCut = "disabled"
      self.loCut = "disabled"
      self.colour = "Pink"

  def askColour(self):
    '''
    Prompt the user to choose a colour noise spectrum scalar
      - "Brownian" uses the reciprocal of the cube root of the frequency
      - "Pink" uses the reciprocal of the square root of the frequency
      - "Velvet" uses the reciprocal of the frequency
    ''' # unfinished feature. Defaults to "Pink"
    self.colour = "Pink"

  def isValidFrequency(self, freq:str) -> bool:
    '''
    Helper function to ensure a user-input is:
      - Only typeof(int)
      - An integer between [0,20K]
    '''
    if (freq.isnumeric() == False):
      return False
    freq = int(freq)
    if (0 < freq <= 20000):
      return True
    return False

  def askCutoffFrequencies(self):
    '''
    Prompt the user to choose hiCut and loCut frequencies for the transformation.
    Frequencies below the loCut will not be transformed.
    Frequencies above the hiCut will not be transformed.
    '''
    validHiCut = False
    validLoCut = False
    print(" RCW uses a reciprocal frequency scalar transformation.")
    print(" This can result in significant loss in apparent loudness.")
    
    while not validLoCut:
      decision = input("\n What is the LOWEST (integer) frequency that you want left unchanged? ").strip()
      self.checkSpecialInput(decision)
      if (self.isValidFrequency(decision)):
        self.loCut = int(decision)
        validLoCut = True
      else:
        print(" Enter a whole number from 1 to 20,000")
    while not validHiCut:
      decision = input(" What is the HIGHEST (integer) frequency that you want left unchanged? ").strip()
      self.checkSpecialInput(decision)
      if (self.isValidFrequency(decision)):
        self.hiCut = int(decision)
        validHiCut = True
      else:
        print(" Enter a whole number from 1 to 20,000")

  def askIfColourize(self):
    '''
    Prompt the user to verify inputted information is as they intended.
    '''
    validInput = False
    while not validInput:
      decision = input("\n If above information is intended...\n Enter 'C' to colourize. Or enter 'R' to restart (C/R): ").lower().strip()
      self.checkSpecialInput(decision)
      if decision == "c":
        validInput = True
        self.submittable = True
      elif decision == "r":
        validInput = True
        self.initializeRepeat()
      else:
        print(" Please input 'C' for Colourize or 'R' for Restart")

  def askIfRepeat(self):
    '''
    Prompt the user to repeat the process or exit.
    '''
    validInput = False 
    while not validInput:
      decision = input("\n Would you like to Transform another digital audio file? (Y/N): ").lower().strip()
      self.checkSpecialInput(decision)
      if decision == "y":
        validInput = True
        self.initializeRepeat()
      elif decision == "n":
        validInput = True
        self.transforming = False
        print(" Goodbye ☺")
      else:
        print(" Please input 'Y' for Yes or 'N' for No")

  def initializeRepeat(self):
    '''
    Recreate start-up state when process occurs in repetition.
    '''
    # file path details (IN & OUT sections)
    self.inFileName = False
    self.outFileName = False
    self.destinationFolderName = False
    self.destinationPath = False

    # rcw transform settings (RCW section)
    self.hiCut = False
    self.loCut = False
    self.colour = False
    self.hasDefault = False

    # sound file details (SND section)
    self.sampleRate = False
    self.channels = False
    self.format = False
    self.soundFile = soundfile.SoundFile
    self.hasSoundFile = False

  def colourize(self):
    '''
    Perform necessary steps to transform inputted digital audio file with the chosen
    colour noise power spectrum as a scalar. The steps are:
      - Read in digital audio data
      - Reshape numpy array as stft expects an inverted format
      - Perform Short-Time Fourier Transform
      - Transform frequencies with colour scalar
      - Invert the Short-Time Fourier Transform
      - Reshape the reshaped dimensions to original matrix indexes
      - Write new file to disk
    '''
    # load audio data from soundfile
    print(" Reading audio data...")
    audioData = self.soundFile.read(always_2d=True)

    # audio data has the inverse dimensions that the fourier function expects as input, must reshape.
    """ Reshape 'F', column-major mode, changes the array from (samples, channels) to
    (channels, samples) where each sample has the left and right sample per homogenous cell. """
    audioData_reshaped = audioData.reshape((2, audioData.size // 2), order='F')

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
    print(" Performing Short-Time Fourier Transform...")
    audioData_stft = librosa.stft(audioData_reshaped, n_fft=n_fft, hop_length=hop_length)

    # the data represents magnitude of frequencies at each frame. 
    # librosa.fft_frequencies gathers which specific frequencies are being represented.
    """ Get frequencies for chosen stft window. """
    lib_freqs = librosa.fft_frequencies(sr=self.soundFile.samplerate, n_fft=n_fft) 

    # convert cutoff defaults to valid integer comparators
    if (self.loCut == "disabled"):
      self.loCut = 0.1
    if (self.hiCut == "disabled"):
      self.hiCut = 10000000 # very large to always be above highest frequency

    # apply hiCut and loCut, no transformation if beyond a cutoff
    for i in range(len(lib_freqs)):
      if (lib_freqs[i] < self.loCut or lib_freqs[i] > self.hiCut):
        lib_freqs[i] = 1

    """ 1/freq ratio for each frequency follow pink noise power spectrum.
        1/sqrt(f) sounds more pink. Not true pink. 
        1/cbrt(f) less pink.                  """
    lib_freqs[0] = 1.0 # avoid divide by zero
    reciprocal_freqs = np.divide(1, np.sqrt(lib_freqs)) # pink-ish, freq = 1/sqrt(freq)
    if (self.loCut == 0.1): # default setting, needs gain enhancement
      reciprocal_freqs *= (np.cbrt(993) // 3) # attempt at maintaining volume after transform 

    # store original range of audio magnitude
    original_min = np.min(audioData_stft)
    original_max = np.max(audioData_stft)

    # multiply the magnitudes of a frequency for every frame according to the
    # prescribed ratio for the weighting of that frequency along the spectrum.
    """ Perform transformation with respect to reciprocal of frequency. """
    print(" Transforming frequency based on colour setting...")
    for i in range(len(audioData_stft[0])):
      # if (reciprocal_freqs[i] > self.loCut and reciprocal_freqs[i] < self.hiCut):
      audioData_stft[0][i] *= reciprocal_freqs[i] # left channel
      audioData_stft[1][i] *= reciprocal_freqs[i] # right channel

    # use original magnitude as a hard limit to transformed magnitude
    audioData_stft.clip(original_min, original_max)
    
    """ Invert the stft transformation. """
    print(" Inverting the Short-Time Fourier Transform...")
    audioData_istft = librosa.istft(audioData_stft, n_fft=n_fft, hop_length=hop_length)

    # re-reshape array dimensions for proper write to file.
    """ Reshape into original shape array before flatten. """
    audioData_transformed = audioData_istft.reshape((audioData_istft.size // 2, 2), order='F')

    """ Write transformed audio to a new file. """
    # with soundfile.SoundFile('NightmaresOnWax_YouWish_pinkish.aiff', 
    print(" Writing new audio file...")
    with soundfile.SoundFile(self.destinationPath, mode='w', samplerate=self.soundFile.samplerate, 
                             channels=self.soundFile.channels, format=self.soundFile.format) as f:
      f.write(audioData_transformed)

    # finished with opened audio file
    self.soundFile.close()



# gets
# SUBMIT?