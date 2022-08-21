import requests
import PyPDF2
import time
import os

def read_pdf():
    filename = 'file.pdf'
    reader = PyPDF2.PdfFileReader(filename)
    pageObj = reader.getNumPages()
    for page_count, i in enumerate(range(pageObj)):
        page = reader.getPage(page_count)
        data = page.extractText()
        wtext = " ".join(data.split())
        ntext = wtext.replace("\n", " ")
        stext = ntext.replace('"', "'")
        ltext = stext.replace('!', r'\!')
        cmd = f"tts --text '{ltext}' --out_path new/{i}fun.wav"
        os.system(cmd)
    print("done")

read_pdf()
# with open('newf.txt', 'r') as n:
#     data = n.read()
#     wtext = " ".join(data.split())
#     ntext = wtext.replace("\n", " ")
#     stext = ntext.replace('"', "'")
#     ltext = stext.replace('!', r'\!')
# cmd = f"tts --text '{ltext}'"
# os.system(cmd)

# with open('file.pdf', 'rb') as file:
#     pdfReader = PyPDF2.PdfFileReader(file)
#     page = pdfReader.getPage(9)
#     text = page.extractText()
#     wtext = " ".join(text.split())
#     ntext = wtext.replace("\n", " ")
#     stext = ntext.replace('"', "'")
#     ltext = stext.replace('!', r'\!')
#     print(ltext)
#     cmd = f"tts --text '{ltext}'"
#     os.system(cmd)
    # with open("page_1.text", "r") as f:
    #     cmd = f'tts --text "{text}"'
    #     os.system(cmd)


    # for t, i in enumerate(split_text):
    #     print(t)
    #     print(i)

    #     params = {
    #         "key": TTS,
    #         "hl": "en-ie",
    #         "c": "MP3",
    #         "f": "16khz_16bit_stereo",
    #         "v": "Oran",
    #         "src": i
    #         }

    #     response = requests.request("GET", url, params=params)

    #     open(f"new/pdf{t}.mp3", "wb").write(response.content)

    #     playsound(f"new/pdf{t}.mp3")
