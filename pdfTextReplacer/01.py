from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

pdf_path = Path(Path.home() / 'Downloads' / '1.pdf')
print(pdf_path)

pdf = PdfFileReader(str(pdf_path))

print(pdf.getNumPages())

for p in pdf.pages:
    with open('buff.txt', 'a') as f:
        f.write(p.extractText())
    