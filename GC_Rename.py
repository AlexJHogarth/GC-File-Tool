# Simple script for converting a folder of Iso files into the Nintendont File structure of /Game_Title/game.iso (or disc2.iso for multi disc games)
# Place script in folder with isos before running or change the file_location variable

import os
from os.path import isfile, join

File_Location = os.path.dirname(os.path.realpath(__file__))

onlyfiles = [f for f in os.listdir(File_Location) if isfile(join(File_Location, f))]
onlyfiles.remove(os.path.basename(__file__))

onlyfiles = [filename for filename in onlyfiles if filename[-4:] == ".iso" ]
for File in onlyfiles:
    Disc = 0
    if "Disc" in File:
        # Assumes file name does not contain "Disc" in the game title
        if "Disc 1" in File:
            Disc = 1
        else:
            Disc = 2


    if Disc == 0:
        New_Dir = File_Location+"\\"+File[0:-4]
    else:
        New_Dir = File_Location+"\\"+File[0:-13]

    if Disc == 1 or Disc == 2:
        if not os.path.isdir(New_Dir):
            os.makedirs(New_Dir)
    else:
        os.makedirs(New_Dir)


    if Disc == 1 or Disc == 0:
        os.rename(File_Location+"\\"+File,New_Dir+"\game.iso")
    elif Disc == 2:
        os.rename(File_Location+"\\"+File,New_Dir+"\disc2.iso")

print("Done!")