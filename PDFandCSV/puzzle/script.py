#%%
# find link
import csv
from os import read

file = open('find_link.csv', encoding='utf-8', mode='r')
reader = csv.reader(file)
i = 0
link = ''
for line in reader:
    link += line[i]
    i+=1
file.close()
print(link)
# %%
import PyPDF2
import re

file = open('find_phone_number.pdf', mode='rb')
reader = PyPDF2.PdfFileReader(file)
pattern = r'\d{3,4}.\d{3,4}.\d{3,4}'
all_text = ''
for page_num in range(reader.numPages):
    page = reader.getPage(page_num)
    page_text = page.extractText()
    all_text += page_text

matches = re.findall(pattern, all_text)
print(matches)
# %%
