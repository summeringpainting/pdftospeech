import PyPDF2
import os

def read_pdf():
    filename = '1984.pdf'
    reader = PyPDF2.PdfFileReader(filename)
    pageObj = reader.getNumPages()
    for page_count, i in enumerate(range(pageObj)):
        page = reader.getPage(page_count)
        data = page.extractText()
        wtext = " ".join(data.split())
        ntext = wtext.replace("\n", " ")
        stext = ntext.replace('"', "'")
        ltext = stext.replace('!', r'\!')
        cmd = f'tts --text "{ltext}" --out_path 1984/{i}fun.wav'
        os.system(cmd)
    print("done")


read_pdf()
