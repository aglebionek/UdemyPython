#%%
import PyPDF2
f = open('Working_Business_Proposal.pdf', 'rb') # read binary
pdf_reader = PyPDF2.PdfFileReader(f)
print(pdf_reader.numPages)

for page_number in range(pdf_reader.numPages):
    page = pdf_reader.getPage(page_number)
    page_text = page.extractText()
    lines = page_text.split('\n')
    for line  in lines:
        print(line)
    #print(page_text)

pdf_write = PyPDF2.PdfFileWriter()
pdf_write.addPage(pdf_reader.getPage(0))
pdf_output = open('some_new_pdf.pdf', 'wb')
pdf_write.write(pdf_output)
pdf_output.close()
