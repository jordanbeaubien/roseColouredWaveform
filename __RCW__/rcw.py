
from userfacing import rcw_interface    # import functions for terminal user interface

interface = rcw_interface()

while (interface.transforming == True):

  # display blank/basic details of current state of process
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


# for each setting, if(self.___) then don't set it
# if all are not unknown (all are known) then ask to submit.


if __name__ == "__main__":
  pass