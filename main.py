import math
from pypdf import PdfWriter, PdfReader

pdf = PdfReader(open("document.pdf", "rb"))
blank_pdf = PdfReader(open("blank_a4.pdf", "rb"))

output_pdf = PdfWriter()

a = len(pdf.pages)
x = math.floor(a / 4)
y = a % 4

i = 0
# TODO: scape before reaching out of index
for n in range(x + 1):
    if i < x:
        output_pdf.add_page(pdf.pages[(4*i)])
        output_pdf.add_page(pdf.pages[(4*i)+2])
        output_pdf.add_page(pdf.pages[(4*i)+3])
        output_pdf.add_page(pdf.pages[(4*i)+1]) 
    if i == x:
        if y == 1:
            output_pdf.add_page(pdf.pages[(4*i)])
            output_pdf.add_page(blank_pdf.pages[0])
            output_pdf.add_page(blank_pdf.pages[0])
            output_pdf.add_page(blank_pdf.pages[0])
        if y == 2:
            output_pdf.add_page(pdf.pages[(4*i)])
            output_pdf.add_page(blank_pdf.pages[0])
            output_pdf.add_page(blank_pdf.pages[0])
            output_pdf.add_page(pdf.pages[(4*i)+1])
        if y == 3:
            output_pdf.add_page(pdf.pages[(4*i)])
            output_pdf.add_page(pdf.pages[(4*i)+2])
            output_pdf.add_page(blank_pdf.pages[0])
            output_pdf.add_page(pdf.pages[(4*i)+1])
        if y == 0:
            output_pdf.add_page(pdf.pages[(4*i)])
            output_pdf.add_page(pdf.pages[(4*i)+2])
            output_pdf.add_page(pdf.pages[(4*i)+3])
            output_pdf.add_page(pdf.pages[(4*i)+1])
    i += 1

with open("document_output.pdf", "wb") as outputStream:
    output_pdf.write(outputStream)