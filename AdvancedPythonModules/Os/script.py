# os and shutil basically allow to manipulate files and folders
f = open('practice.txt', 'w+') #w for write, + to create a file if it doesn't exist
f.write('test string')
f.close()

import os
print(os.getcwd()) #cwd - current working directory
print(os.listdir()) #lists everything in the current working directory if no argument given
print(os.listdir('/home/aglebionek/UdemyPython')) #lists everything in provided directory, if it exists

import shutil
#shutil.move('practice.txt', '/home/aglebionek') #moves file from cwd to a chosen location, kinda linux's mv command
#os.unlink('path_to_file') removes a file
#os.rmdir('dir') removes dir
#shutil.rmtree('path') removes folder and files inside

#it's basically tree command in Linux (or ls -R)
for folder, sub_folders, files in os.walk('/home/aglebionek/UdemyPython'):
    print(f'Currently looking at: {folder}')
    print(f'The subfolders are:')
    for sub_folder in sub_folders:
        print(f'\t{sub_folder}')
    print('The files are:')
    for file in files:
        print(f'\t{file}')
    