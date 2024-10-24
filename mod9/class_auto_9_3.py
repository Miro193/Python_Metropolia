# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän. 
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa 
# tuntimäärässä edennyt. Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. 
# Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

class Auto:

	def __init__(self, rekisteritunnus, huippunopeus, hetkellinen_nopeus = 0, kuljettu_matka = 0):
		self.rekisteritunnus = rekisteritunnus
		self.huippunopeus = huippunopeus
		self.hetkellinen_nopeus = hetkellinen_nopeus
		self.kuljettu_matka = kuljettu_matka

	def kiihdytaa(self, nopeuden_muutos):
		if nopeuden_muutos > 0 and nopeuden_muutos <= self.huippunopeus and self.hetkellinen_nopeus <= self.huippunopeus:
			self.hetkellinen_nopeus += nopeuden_muutos
		else:
			self.hetkellinen_nopeus = 0

	
	def kulje(self, tuntimaara):
		self.kuljettu_matka += self.hetkellinen_nopeus * tuntimaara



uusi_auto = Auto("ABC-123", 142, 0, 2000)

print(f"""\nrekisterinumero = {uusi_auto.rekisteritunnus}
huippunopeus = {uusi_auto.huippunopeus} km/h
hetkellinennopeus = {uusi_auto.hetkellinen_nopeus} km/h
kuljettu matka = {uusi_auto.kuljettu_matka} km""")
print("\n---------------\n")

uusi_auto.kiihdytaa(60)
print(f"Auton nopeus = {uusi_auto.hetkellinen_nopeus} km/h")

uusi_auto.kulje(1.5)
print(f"Auton tämän hetken kuljettu matka on {uusi_auto.kuljettu_matka} km")
