import os

listOfFolders = ["Pythons","JavaScript","C++","C","Dart","PHP","Kotlin","Bash","Java","Matlab","SQL"]

for folderName in listOfFolders:
    os.makedirs(folderName)