import requests

url = "https://maptiles.p.rapidapi.com/es/map/v1/3/4/2.png"

headers = {
	"X-RapidAPI-Key": "get-key",
	"X-RapidAPI-Host": "maptiles.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)