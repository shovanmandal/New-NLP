import PyPDF2
import re
import docx


f= open('sample.docx','rb')
c= f.read()
print(type(c))

#print(readDocx.getText('sample.docx'))

#doc = docx.Document('sample.docx')



'''
def file_open():

     file_name = input('Pease insert the file name:')
     file_content = ''

     if file_name.endswith('.pdf'):
          pdf_file = open(file_name,'rb')                        #Reading PDF file
          read_pdf = PyPDF2.PdfFileReader(pdf_file)
          number_of_pages = read_pdf.getNumPages()
          page = read_pdf.getPage(0)
          file_content = page.extractText()

     elif file_name.endswith('.txt'):
          file = open(file_name, "r")                        # Reading Text file
          file_content = file.read()

     cleanString = re.sub('\W+',' ', file_content )            #cleanse the unwanted expressions
     cleanString = cleanString.lower()
     print(cleanString)

file_open()
'''
