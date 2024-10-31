# Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle. 
# Käytä seuravalla sivulla esiteltävää rajapintaa: https://api.chucknorris.io/. 
# Käyttäjälle on näytettävä pelkkä vitsin teksti.

import requests
import json

hakusana = int(input("Valitse montako satunnaista Chuck Norris vitsiä haluat 1-10: "))

print("")
num = 0
for i in range(hakusana):
	num += 1
	# url pyyntö
	pyyntö = "https://api.chucknorris.io/jokes/random"
	vastaus = requests.get(pyyntö)
	data = vastaus.json()
	print(f"{num} - {data["value"]}")
