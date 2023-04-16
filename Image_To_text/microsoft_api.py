import requests

api = "https://microsoft-computer-vision3.p.rapidapi.com/analyze"

languages = ['en', 'es', 'ja', 'pt', 'zh']

querystring = {"language":languages[0],"visualFeatures[0]":"Tags"}

payload = {"url": "https://cdn.discordapp.com/attachments/915276863272800297/1096930577682288780/2Q.png"}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "6dbf679bb0msh9a5b24765635297p1f0e7fjsn9317aec4a187",
	"X-RapidAPI-Host": "microsoft-computer-vision3.p.rapidapi.com"
}

response = requests.request("POST", api, json=payload, headers=headers, params=querystring)

print(response.text)