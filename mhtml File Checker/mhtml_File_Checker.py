'''
mhtml File Checker

Created on Jan 19, 2018
@author: Jonathan Tang
'''

import os
def getDirlist(path):
    """Return a sorted list of all entries in path.
    This returns just the names of entries, not the full path to the names"""
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist


def getFileType(fileName):
    """Returns a string of the file type of a file, without the preceeding dot,
        ex: "doc", "jpeg","mhtml"
        Input fileName should be a string, either a simple file name or a full path"""
    index = -1  #Only Python allows negative indices
    fileType = ""
    while True:  #Get the file type
        letter = fileName[index]
        if letter == ".":
            break  #fileType is complete (doesn't include the ".")
        else:
            fileType = letter + fileType  #build fileType by concatenate strings
            index -= 1

def verifyDesiredFiles(path):
    """Check if the given directory and any subdirectories contain any
        .mhtml files with a file size below 50 000 bytes.
        Currently implemented to detect improperly saved ILC lesson pages"""
    minFileSize = 50000  #50 000 bytes
    dirlist = getDirlist(path)
    for f in dirlist:
        fullname = os.path.join(path, f)  #Turn name into full pathname
        if os.path.isdir(fullname):  #If a directory, recurse
            verifyDesiredFiles(fullname)
        else:  #The path is a file
            #print(f)
            try:
                fileType = getFileType(f)
                if fileType in ("mhtml"):  #Only check the file types listed in the tuple
                    fileSize = os.stat(fullname).st_size
                    if fileSize < minFileSize:  #Because properly saved .mhtml files from ILC lesson pages should be larger than this
                        print("Warning: '{0}' only {2} bytes, may be corrupt ({1})".format(f,fullname,fileSize))
            except:  #Ignore files and scripts without a type extension
                #print(fullname)
                pass

          
pathStr = input("Please enter the full file path of the desired directory: ")
verifyDesiredFiles(pathStr)
print("verifyDesiredFiles() Done")
