import requests
import random 


<html>
</html>

print("Please choose your first airport! (The Departure Flight)")
location1 = input()

print("Please choose your second airport! (The Arrival Flight)")
location2 = input()

locations = [location1, location2]



url = "https://maptiles.p.rapidapi.com/es/map/v1/3/4/2.png"

headers = {
	"X-RapidAPI-Key": "get-key",
	"X-RapidAPI-Host": "maptiles.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)

for maps in map()
	while 



<script>
const Maps