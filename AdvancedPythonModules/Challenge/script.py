#import zipfile
#search_in_archive = zipfile.ZipFile('unzip_me_for_instructions.zip', 'r')
#search_in_archive.extractall('extracted')

import os
import re

path = f'{os.getcwd()}/extracted/extracted_content'

with open(f'{path}/Instructions.txt', 'r') as f:
    for line in f:
        print(line)

pattern = r'\d{3}-\d{3}-\d{4}'

matches = list()
def search_in_files(dir, pat):
    global matches
    # it auto recurses
    for folder_path, _, files in os.walk(dir):
        for file in files:
            with open(f'{folder_path}/{file}', 'r') as f:
                for line in f:
                    found = re.findall(pat, line)
                    if found: 
                        matches.append(found)
                        matches.append(f'{folder_path}/{file}')
                f.close()

search_in_files(path, pattern)

print(matches)
