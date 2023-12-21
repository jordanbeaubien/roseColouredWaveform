# ------------------------------------------------- #
#  Process : roseColouredWaveform
#  Author  : Jordan Beaubien; December 20th, 2023
#  Usage   : Ualberta MUSIC 645 Final Project
#  Prof.   : Dr. Scott Smallwood
# ------------------------------------------------- #

from userfacing import rcw_interface    # import class for terminal user interface


def roseColouredWaveform(): 
  '''
  RCW (Rose Coloured Waveform) is a terminal application that receives a digital audio 
  file/waveform as input and outputs a version of the given audio recording where all 
  present frequencies have been transformed using the pink noise power spectrum as a scalar.
  '''

  # create an instance of the interface
  interface = rcw_interface()

  # while a user is transforming a digital sound file
  while (interface.transforming == True):

    # display blank/basic details of current state of process
    interface.displayInterface()

    # ensure a valid path is provided to a valid digital sound file
    while (interface.hasSoundFile == False):
      interface.getInputFile()
    interface.displayInterface()

    # set the colour noise spectrum, hiCut and loCut configuration
    interface.setDefault()
    if (interface.hasDefault == False):
      interface.askColour()
      interface.askCutoffFrequencies()
    interface.displayInterface()

    # get filename of resultant digital audio file
    interface.getOutFileName()
    interface.displayInterface()

    # ask user to verify inputted information is acceptable (submittable)
    interface.askIfColourize()
    if interface.submittable:
      interface.colourize()
      print("\n Successful transform. Please find your new audio with this file path.")
      print(" " + interface.destinationPath)
      print(" [!!] WARNING: Non-default hiCut & loCut files are LOUDER than default-set files.")
      interface.askIfRepeat()

if __name__ == "__main__":
  roseColouredWaveform()