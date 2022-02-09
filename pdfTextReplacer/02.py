from tika import parser

raw = parser.from_file("1.pdf")
with open('buff.txt', 'w') as f:
    f.write(raw['content'])