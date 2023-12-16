import transformation
import soundfile            


class rcw_interface:
  def __init__(self):
    # file path details (IN & OUT sections)
    self.inFileName = False
    self.outFileName = False
    self.destinationFolderName = False
    self.destinationFolderPath = False

    # rcw transform settings (RCW section)
    self.hiCut = False
    self.loCut = False
    self.colour = False

    # sound file details (SND section)
    self.sampleRate = False
    self.channels = False
    self.format = False
    self.soundFile = soundfile.SoundFile
    self.hasSoundFile = False

  # print the user interface here
  def displayInterface(self):

    print("\n" * 40)
    print("  8888888b.   .d8888b.  888       888")
    print("  888   Y88b d88P  Y88b 888   o   888")
    print("  888    888 888    888 888  d8b  888")
    print("  888   d88P 888        888 d888b 888")
    print("  8888888P   888        888d88888b888")
    print("  888 T88b   888    888 88888P Y88888")
    print("  888  T88b  Y88b  d88P 8888P   Y8888")
    print("  888   T88b   Y8888P   888P     Y888")
    print("\n")

    print(" -------------------------------------")
    
    ##### IN #####
    ##### IN #####
    if (self.inFileName): # display user-provided pre-transformation file
      print(" | [✔] | Operand File:   | " + self.inFileName)
    else:
      print(" | [ ] | Operand File:   | (unknown)       ")
    print(" -------------------------------------")
    
    ##### RCW #####
    ##### RCW #####
    if (self.colour): # display noise power spectrum colour setting
      print(" |  R  | Colour Setting: | " + self.colour)
    else:
      print(" |  R  | Colour Setting: | (unknown)       ")
    if (self.hiCut):  # display user-chosen hi-frequency cutoff of the transformation
      print(" |  C  | Hi-Freq Cut-off | " + str(self.hiCut))
    else:
      print(" |  C  | Hi-Freq Cut-off | (unknown)       ")
    if (self.loCut):  # display user-chosen lo-frequency cutoff of the transformation
      print(" |  W  | Lo-Freq Cut-off | " + str(self.loCut))
    else : 
      print(" |  W  | Lo-Freq Cut-off | (unknown)       ")
    print(" -------------------------------------")
    
    ##### SND #####
    ##### SND #####
    if (self.hasSoundFile): # display file-decoded audio format
      # print(" |  S  | AudioFormat:    | " + self.format)
      print(" |  S  | AudioFormat:    | " + self.soundFile.format)
    else:
      print(" |  S  | AudioFormat:    | (unknown)")
    if (self.hasSoundFile): # display file-decoded channel count
      # print(" |  N  | Channels:       | " + str(self.channels))
      print(" |  N  | Channels:       | " + str(self.soundFile.channels))
    else: 
      print(" |  N  | Channels:       | (unknown)")
    if (self.hasSoundFile): # display file-decoded sample rate
      # print(" |  D  | SampleRate:     | " + str(self.sampleRate))
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
    if (self.outFileName):  # display user-chosen name of file
      # print(" |  O  | Resultant name: | " + self.outFileName)
      print(" |  O  | Resultant File: | " + self.outFileName)
    else: 
      print(" |  O  | Resultant File: | (unknown)       ")
    print(" -------------------------------------")


  def getInputFile(self):
    print("\n")
    inputFilePath = input("   What file would you like to transform?").strip().split("/")

    self.inFileName = inputFilePath.pop(-1)
    self.destinationFolderName = inputFilePath[-1] + "/"
    self.destinationFolderPath = "/".join(inputFilePath) + "/"
    # self.outFileName = "/".join(inputFilePath) + "/" # TESTING

  def setDefault(self):
    validInput = False
    print("\n")
    while not validInput:
      userInput = input("    Would you like to use the default values? (Y/N)").lower().strip()
      if userInput == "y":
        validInput = True
        hasDefault = True
      elif userInput == "n":
        validInput = True
        hasDefault = False
      else:
        print("   Please input 'Y' for Yes or 'N' for No")
    if hasDefault:
      self.hiCut = 20000
      self.loCut = -1
      self.colour = "Pink"



# gets


# ORIGINAL FILE PATH
# COLOUR TYPE
# HiCUT 
# LoCUT
# FUTURE FILE NAME
# SUBMIT?