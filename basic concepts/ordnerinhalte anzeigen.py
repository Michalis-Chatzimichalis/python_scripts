import os

#cd pwd
os.chdir('/Users/mic/OneDrive/Documents')

#Specify the directory and open it
path = '/Users/mic/OneDrive/Documents/Steuern'
directory = os.listdir(path)

#call the variable
for directory in path:
    open (directory)