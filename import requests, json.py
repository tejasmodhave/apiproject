import requests, json
apiKey = "faa29dc3b49318a825c36824773abb46"
baseURL = "https://api.openweathermap.org/data/2.5/weather?q="
cityname = input("Enter the city name : ")
Urll = baseURL + cityname +"&appid=" + apiKey
response = requests.get(Urll)
data = response.json()
print("Current temperature",data["main"]["temp"])
print("Minimum temperature",data["main"]["temp_min"])
print("Maximum temperature",data["main"]["temp_max"])
