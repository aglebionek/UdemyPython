f = open('file1.txt', 'w+')
f.write('one file')
f.close()

f = open('file2.txt', 'w+')
f.write('two file')
f.close()

# lets say we want to zip the files above
import zipfile
compressed_file = zipfile.ZipFile('comp_file.zip', 'w')
compressed_file.write('file1.txt', compress_type=zipfile.ZIP_DEFLATED)
compressed_file.write('file2.txt', compress_type=zipfile.ZIP_DEFLATED)
compressed_file.close()
