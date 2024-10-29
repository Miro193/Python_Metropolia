
# Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi, 
# pituus kilometreinä ja osallistuvien autojen lista. Luokassa on alustaja, joka saa parametreinaan nimen, 
# kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:

#    tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet 
#    eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
#    tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
#    kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun 
#    kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.

# Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli". Luotavalle kilpailulle annetaan kymmenen 
# auton lista samaan tapaan kuin aiemmassa tehtävässä. Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa 
# tunti_kuluu-metodia, jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi. 
# Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.
from random import randint, randrange
from prettytable import PrettyTable
# from mod9.class_auto_9_4 import Auto

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
			
	def kulje(self, tuntimaara):
		self.kuljettu_matka += self.hetkellinen_nopeus * tuntimaara

class Kilpailu:
	kilpa_autot = []
	matka = 0

	def __init__(self, nimi, pituus_km, autot):
		self.nimi = nimi
		self.pituus_km = pituus_km
		self.autot = autot

		for numero in range(1, autot+1):
			nopeus = randint(100,200)
			kilpa_auto = Auto(f"ABC-{numero}", nopeus)
			Kilpailu.kilpa_autot.append(kilpa_auto)

	def tunti_kuluu(self):
		for h in self.kilpa_autot[:]:
			h.kiihdytaa(randrange(-10,15))
			h.kulje(1)
			if h.kuljettu_matka > Kilpailu.matka:
				Kilpailu.matka = h.kuljettu_matka

	def tulosta_tilanne(self):
		table = PrettyTable()
		table.field_names = ["Rekisteritunnus", "Huippunopeus", "Hetkellinen nopeus", "Kuljettu matka"]
		n = 0

		for k in Kilpailu.kilpa_autot[:]:
			n += 1
			auto_lista = [k.rekisteritunnus, k.huippunopeus, k.hetkellinen_nopeus,k.kuljettu_matka]
			table.add_row(auto_lista)
		print(table)

	def kilpailu_ohi(self):
		if Kilpailu.matka > self.pituus_km:
			return True
		return False

##### Pääohjelma ######

kilpailu = Kilpailu("Suuri romuralli", 8000, 10)
print("\n*KILPAILUN ALOITUS*")
kilpailu.tulosta_tilanne()
ohi_on = False
kisataulu = "Kisataulukko"

while ohi_on != True:

	for tunti in range(11):
		kilpailu.tunti_kuluu()
		
		if kilpailu.kilpailu_ohi() == True:
			ohi_on = True

	print(f"\n{kisataulu}\n{kilpailu.nimi} kilpailun tulosten tarkistus {tunti} tunnin jälkeen.")
	kilpailu.tulosta_tilanne()

print(f"\n{kilpailu.nimi}n kilpailun lopputulos.")
kilpailu.tulosta_tilanne()