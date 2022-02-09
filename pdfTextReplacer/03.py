import PyPDF2

pdf = open('1.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdf)
print(pdfReader.numPages)

num = pdfReader.numPages

for a in range(0,num):
    text = ""

    page = pdfReader.getPage(a)
    text += page.extractText().encode('ascii', 'ignore').decode('ascii')
    # .decode('ascii')

    with open('buff.txt', 'a') as f:
        f.write(text)