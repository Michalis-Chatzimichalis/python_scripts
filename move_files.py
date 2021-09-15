import os
import shutil

#Move app files with .msi or .exe to Application folder
os.rename('Users/apoll/Downloads/wsl_update_x64.msi', '/Users/apoll/Downloads/Applications')

#os.rename('C:\Users\apoll\Downloads\*.exe', 'C:\Users\apoll\Downloads\Applications') 