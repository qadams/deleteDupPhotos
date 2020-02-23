import os
import re
import sys

searchRootDir = sys.argv[1]
fileList = []
filenamePattern = ".*\ \(\d*\)\.[A-za-z]*"

for root, dirs, files in os.walk(searchRootDir, topdown=False):
    for name in files:
        fileX= os.path.join(root, name)
        match = re.match(filenamePattern, fileX)
        if match:
            print(fileX)
