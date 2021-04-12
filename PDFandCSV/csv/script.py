#%%
import csv

data = open("example.csv", encoding='utf-8')

csv_data = csv.reader(data)

data_lines = list(csv_data)

all_emails = list()
for line in data_lines[1:]:
    all_emails.append(line[3])

full_names = list()
for line in data_lines[1:]:
    full_names.append((line[1], line[2]))

file_to_output = open('to_save_file.csv', mode='a+', newline='') # a for append
csv_writer = csv.writer(file_to_output, delimiter=',')
csv_writer.writerow(['a', 'b', 'c'])
csv_writer.writerow([1,2,3])
file_to_output.close()
# %%
