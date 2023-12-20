import transformation
import soundfile            


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
      print(" |  C  | Hi-Freq Cut-off | " + str(self.hiCut))
    else:
      print(" |  C  | Hi-Freq Cut-off | (unknown)       ")
    if (self.loCut):                  # display user-chosen lo-frequency cutoff of the transformation
      print(" |  W  | Lo-Freq Cut-off | " + str(self.loCut))
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



# gets


# ORIGINAL FILE PATH
# COLOUR TYPE
# HiCUT 
# LoCUT
# FUTURE FILE NAME
# SUBMIT?