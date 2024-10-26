# Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan 
# nopeuden muutoksen (km/h). Jos nopeuden muutos on negatiivinen, auto hidastaa. 
# Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa. Auton nopeus ei saa kasvaa 
# huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi. Jatka pääohjelmaa siten, 
# että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h. 
# Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h 
# ja tulosta uusi nopeus. Kuljettua matkaa ei tarvitse vielä päivittää.

# (rekisteritunnus ABC-123, huippunopeus 142 km/h)

class Auto:

	def __init__(self, rekisteritunnus, huippunopeus, hetkellinen_nopeus = 0, kuljettu_matka = 0):
		self.rekisteritunnus = rekisteritunnus
		self.huippunopeus = huippunopeus
		self.hetkellinen_nopeus = hetkellinen_nopeus
		self.kuljettu_matka = kuljettu_matka

	def kiihdytaa(self, nopeuden_muutos):
		self.hetkellinen_nopeus += nopeuden_muutos
		if self.hetkellinen_nopeus < 0:
			self.hetkellinen_nopeus = 0
		if self.hetkellinen_nopeus > self.huippunopeus:
			self.hetkellinen_nopeus = self.huippunopeus

		
uusi_auto = Auto("ABC-123", 142)

print(f"""\nrekisterinumero = {uusi_auto.rekisteritunnus}
huippunopeus = {uusi_auto.huippunopeus} km/h
hetkellinennopeus = {uusi_auto.hetkellinen_nopeus} km/h
kuljettu matka = {uusi_auto.kuljettu_matka} km""")
print("\n---------------\n")

uusi_auto.kiihdytaa(30)
uusi_auto.kiihdytaa(70)
uusi_auto.kiihdytaa(50)
print(f"Auton nopeus = {uusi_auto.hetkellinen_nopeus} km/h")
uusi_auto.kiihdytaa(-200)
print(f"Auton nopeus = {uusi_auto.hetkellinen_nopeus} km/h")