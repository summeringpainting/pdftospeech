import requests

url = "https://voicerss-text-to-speech.p.rapidapi.com/"

querystring = {"key":"e8385e6835b244af8210993645a8e163"}

payload = "f=8khz_8bit_mono&c=mp3&r=0&hl=en-us&src=Hello%2C%20world!"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "227a43e521mshe30a9a539b340c4p1f84bbjsne9eea132a7c6",
	"X-RapidAPI-Host": "voicerss-text-to-speech.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)
