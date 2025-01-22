from pypdf import PdfWriter, PdfReader

even_pdf = PdfReader(open("document_even.pdf", "rb"))
odd_pdf = PdfReader(open("document_odd.pdf", "rb"))

output = PdfWriter()

ev = 0
od = 0

print(len(even_pdf.pages)++len(odd_pdf.pages))

for i in range(len(even_pdf.pages)++len(odd_pdf.pages)):
    if i%2 == 1:
        if ev < len(even_pdf.pages):
            output.add_page(even_pdf.pages[ev])
            print("ev")
            ev = ev + 1
    if i%2 == 0:
        if od < len(odd_pdf.pages):
            output.add_page(odd_pdf.pages[od])
            print("od")
            od = od + 1

with open("document.pdf", "wb") as outputStream:
    output.write(outputStream)
        