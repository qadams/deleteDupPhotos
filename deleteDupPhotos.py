import os
import fnmatch
import sys

searchRootDir = sys.argv[1]
filenamePattern = '[a-zA-Z0-9]*([0-9]+)*.[a-zA-Z]*'
#filenamePattern = '[a-zA-Z0-9_]*([0-9]+)*[a-zA-Z0-9_]*'

files = os.listdir(searchRootDir)
duplicateFiles = fnmatch.filter(files, filenamePattern)

for duplicateFile in duplicateFiles:
    print(duplicateFile)

#print(duplicateFile) for duplicateFile in duplicateFiles
#os.remove(duplicateFile) for duplicateFile in duplicateFiles
