# mhtml File Checker

A short program used to check .mhtml files generated from saving webpages as "Webpage, Single File" in Google's Chrome browser. Using recursion to completely traverse the given entire directory and its sub-directories, the program checks whether any .mhtml files encountered have a file size < 50 000 KB, as the small file size would likely mean that the file is corrupt or improperly saved. The program could be modified to check for other attributes for other types of files. Uses Python's `os` module.

Written and run under Python 3.5.2
