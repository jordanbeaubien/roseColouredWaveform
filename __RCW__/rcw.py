

# import functions for terminal user interface
from userfacing import rcw_interface

import transformation   # import functions sound transforming


interface = rcw_interface()
interface.displayInterface()

# get input filename
# print("\n")
while (interface.hasSoundFile == False):
  interface.getInputFile()
  
interface.displayInterface()

# user default settings?
interface.setDefault()
interface.displayInterface()

interface.getOutFileName()
interface.displayInterface()

# for each setting, if(self.___) then don't set it

# if all are not unknown (all are known) then ask to submit.


if __name__ == "__main__":
  pass