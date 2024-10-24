# Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi. 
# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta. 
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. 
# Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa. 
# Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

#	Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä. 
#	Tämä tehdään kutsumalla kiihdytä-metodia. Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. 
#	Tämä tehdään kutsumalla kulje-metodia.

# Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä. 
# Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.
from random import randint, randrange

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


kilpa_autot = []
matka = 0
for i in range(1,11):
	numero = i
	nopeus = randint(100,200)
	kilpa_auto = Auto(f"ABC-{numero}", nopeus)
	kilpa_autot.append(kilpa_auto)
	

while matka <= 1000:

	for h in kilpa_autot[:]:
		h.kiihdytaa(randrange(-10,15))
		h.kulje(1)
		print(h.hetkellinen_nopeus, h.rekisteritunnus, h.kuljettu_matka)
		if h.kuljettu_matka > matka:
			matka = h.kuljettu_matka

for k in kilpa_autot[:]:
	print("------------------------------")
	print(f"  rekisterinumero = {k.rekisteritunnus}\n  huippunopeus = {k.huippunopeus} km/h\n  hetkellinennopeus = {k.hetkellinen_nopeus} km/h\n  kuljettu matka = {k.kuljettu_matka} km")


# uusi_auto.kiihdytaa(60)
# print(f"Auton nopeus = {uusi_auto.hetkellinen_nopeus} km/h")

# uusi_auto.kulje(1.5)
# print(f"Auton tämän hetken kuljettu matka on {uusi_auto.kuljettu_matka} km")