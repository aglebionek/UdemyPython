f = open('file1.txt', 'w+')
f.write('one file')
f.close()

f = open('file2.txt', 'w+')
f.write('two file')
f.close()

# lets say we want to zip the files above
import zipfile
compressed_file = zipfile.ZipFile('comp_file.zip', 'w') # write to archive
compressed_file.write('file1.txt', compress_type=zipfile.ZIP_DEFLATED)
compressed_file.write('file2.txt', compress_type=zipfile.ZIP_DEFLATED)
compressed_file.close()

zip_obj = zipfile.ZipFile('comp_file.zip', 'r') # read archive
zip_obj.extractall('extracted_content') # extract it's content to a folder called extracted_content

import shutil
dir_to_zip = '/home/aglebionek/UdemyPython/AdvancedPythonModules/Zipping/extracted_content'
output_filename = 'example'
shutil.make_archive(output_filename, 'zip', dir_to_zip)
shutil.unpack_archive('example.zip', 'final_uznip', 'zip')