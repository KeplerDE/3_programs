# pip install pypdf2
from PyPDF2 import PdfFileWriter, PdfFileReader
from getpass import getpass


pdfwriter = PdfFileWriter()
pdf = PdfFileReader('resume.pdf')

# for page in range(pdf.numPages):
#     pdfwriter.add_page(pdf.pages[page])

password = getpass(prompt='Введите пароль: ')
pdfwriter.encrypt(password)

with open('protected.pdf', 'wb', encoding='utf-8') as file:
    pdfwriter.write(file)





