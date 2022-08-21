import PyPDF2
import os

filename = 'file.pdf'
reader = PyPDF2.PdfFileReader(filename)
pageObj = reader.getNumPages()
p1 = reader.getPage(2)
data = p1.extractText()
wtext = " ".join(data.split())
print(wtext)
cmd = f"tts --text '{wtext}' --out_path drum.wav"
os.system(cmd)
