# Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api. Kirjoita ohjelma, 
# joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina. 
# Perehdy rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen, 
# jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key). 
# Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.
# --------------------------------------------------------------------- #

import requests
import json

api_key = "35d0b88eef3d38edd221dff96e640f7e"
paikkakunta = input("Anna paikkakunta: ")
pyynto = "https://api.openweathermap.org/data/2.5/weather?"
url = pyynto + "q=" + paikkakunta + "&appid=" + api_key + "&units=metric"
vastaus = requests.get(url)
data = vastaus.json()
# print(json.dumps(data, indent = 2))

print("------------------------------")
print("PÄIVÄN SÄÄ")
print(f"Kaupunki : {data["name"]}")
for a in data["weather"]:
	print(f"Ilma on : {a["description"]} ja pilvisyys {data["clouds"]["all"]}%")
print(f"Ilmankosteus : {data["main"]["humidity"]}")
print(f"Lämpötila on : {data["main"]["temp"]:.1f}C astetta\nPäivän min : {data["main"]["temp_min"]:.1f}C astetta\nPäivän max : {data["main"]["temp_max"]:.1f}C astetta")
print("------------------------------")