import PyPDF2
file= input('file name:')
pdf_file = open(file,'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
print(read_pdf)
number_of_pages = read_pdf.getNumPages()
print(number_of_pages)
page = read_pdf.getPage(0)
page_content = page.extractText()
print (page_content)


