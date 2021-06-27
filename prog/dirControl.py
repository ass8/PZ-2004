#!/usr/bin/python
import os
import os.path
from os import path

def invalidInput():
    print("Invalid input, please try again.\n")
    quit()

systemDetect=os.name
if systemDetect!='posix':
    print("Program is oriented on the UNIX systems.\n")
    quit()

defaultName="~/newFoldersDir"

 print ("File exists:"+str(path.exists('newFoldersDir')))

if path.exists(defaultName)==True and path.isdir(defaultName)==True:
    print("Already exists.\n")
else:
    createDefault="sudo mkdir ~/newFoldersDir"
    os.system(createDefault)

print("List of options:\n\t1)Create a new directory\n\t2)Remove a directory")
choise=int(input("Select option: "))
if choise<1 or choise>3:
    invalidInput()
elif choise==1:
    print("All the directories would be created in the /home/(user)/newFoldersDir directory.\n")
    strDir="sudo mkdir ~/newFoldersDir/"
    dirName=str(input("Enter a name of the directory which will be created: "))
    createDir=strDir+dirName
    os.system(createDir)
elif choise==2:
    print("w8")