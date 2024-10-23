# Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus,
# tämänhetkinen nopeus ja kuljettu matka. Kirjoita luokkaan alustaja, joka asettaa 
# ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin. 
# Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi. 
# Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h). 
# Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

class Auto:
	def __init__(self, rekisteritunnus, huippunopeus, hetkellinen_nopeus = 0, kuljettu_matka = 0):
		self.rekisteritunnus = rekisteritunnus
		self.huippunopeus = huippunopeus
		self.hetkellinen_nopeus = hetkellinen_nopeus
		self.kuljettu_matka = kuljettu_matka

	
uusi_auto = Auto("ABC-123", 142)

print(f"""rekisterinumero = {uusi_auto.rekisteritunnus}
huippunopeus = {uusi_auto.huippunopeus} km/h
hetkellinennopeus = {uusi_auto.hetkellinen_nopeus} km/h
kuljettu matka = {uusi_auto.kuljettu_matka} km""")

