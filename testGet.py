import requests
from playsound import playsound
import PyPDF2
import time
import os

TTS = os.environ["TTS_KEY"]

url = "http://api.voicerss.org/"


with open('file.pdf', 'rb') as file:
    pdfReader = PyPDF2.PdfFileReader(file)
    page = pdfReader.getPage(7)
    text = page.extractText()
    wtext = " ".join(text.split())
    ntext = wtext.replace("\n", " ")
    split_text = ntext.split('.')

    for t, i in enumerate(split_text):
        print(t)
        print(i)

        params = {
            "key": TTS,
            "hl": "en-ie",
            "c": "MP3",
            "f": "16khz_16bit_stereo",
            "v": "Oran",
            "src": i
            }

        response = requests.request("GET", url, params=params)

        open(f"new/pdf{t}.mp3", "wb").write(response.content)

        playsound(f"new/pdf{t}.mp3")

