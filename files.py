import os
import sys


#file name
filename = "/file.txt"

#directory name
directory = "Downloads"

#gets you to the home directory
home_dir = os.path.expanduser('~')
print(home_dir)

#joins the home directory to the directory
path =  os.path.join(home_dir,directory)
print(path)

#creates the whole path and filename
filename = path + filename
print(filename)

#checks if the path is there
isDir = os.path.isdir(path)

checks if the file is there
isFile =  os.path.isfile(filename)

#if file is not here print and error to the screen
if isFile == False:
	sys.exit("File does not exist")
	
#if directory is not there create it
if isDir == False:
    os.mkdir(savePath)

#open a file and work with it , a = append, w = write
f = open(filename, 'a')
    f.write('something')
    f.close
