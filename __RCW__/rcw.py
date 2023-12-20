

# import functions for terminal user interface
from userfacing import rcw_interface

interface = rcw_interface()

while (interface.transforming == True):

  interface.displayInterface()

  while (interface.hasSoundFile == False):
    interface.getInputFile()
  interface.displayInterface()

  # colour noise spectrum, hiCut & loCut configuration
  interface.setDefault()
  if (interface.hasDefault == False):
    interface.askColour()
    interface.askCutoffFrequencies()
  interface.displayInterface()

  interface.getOutFileName()
  interface.displayInterface()

  interface.colourize()
  print("\n Successful transform. Please find your new audio with this file path.")
  print(" " + interface.destinationPath)
  interface.askIfRepeat()





# for each setting, if(self.___) then don't set it
# if all are not unknown (all are known) then ask to submit.


if __name__ == "__main__":
  pass