
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
			# numero = i
			nopeus = randint(100,200)
			kilpa_auto = Auto(f"ABC-{numero}", nopeus)
			Kilpailu.kilpa_autot.append(kilpa_auto)
			# print(f"{vars(Auto(f"ABC-{numero}", nopeus))}")


	def tunti_kuluu(self):
		for h in self.kilpa_autot[:]:
			h.kiihdytaa(randrange(-10,15))
			h.kulje(1)
			# print(h.hetkellinen_nopeus, h.rekisteritunnus, h.kuljettu_matka)
			if h.kuljettu_matka > self.matka:
				self.matka = h.kuljettu_matka

	def tulosta_tilanne(self):
		lista_autoista = []
		table = PrettyTable()
		table.field_names = ["Rekisteritunnus", "Huippunopeus", "Hetkellinen nopeus", "Kuljettu matka"]
		# table2 = PrettyTable(lista_autoista)
		n = 0
		# print(table)
		for k in Kilpailu.kilpa_autot[:]:
			n += 1
			auto_lista = [k.rekisteritunnus, k.huippunopeus, k.hetkellinen_nopeus,k.kuljettu_matka]
			# print(PrettyTable(auto_lista))
			# lista_autoista.append(auto_lista)
			# lista_autoista.append(k)
			table.add_row(auto_lista)
		print(table)
			# lista_autoista.sort(key=Auto.kuljettu_matka)	
			# print("------------------------------")
			# print(f"  rekisterinumero = {k.rekisteritunnus}\n  huippunopeus = {k.huippunopeus} km/h\n  hetkellinennopeus = {k.hetkellinen_nopeus} km/h\n  kuljettu matka = {k.kuljettu_matka} km")
			# print(vars(k))
			# print(lista_autoista)
			# print(f" Auto:{lista_autoista[n-1][0]}, Kulkenut {lista_autoista[n-1][3]}km")
		# tulos = lista_autoista.sort(key=lista_autoista[:][3])
		# print(lista_autoista[:][:])
		# print(vars(Kilpailu.kilpa_autot.sort(key=k.kuljettu_matka)))
		# print(PrettyTable(lista_autoista))
		# print(vars(lista_autoista[:]))	

	def kilpailu_ohi(self):
		if self.matka <= self.pituus_km:
			return False
		return True

##### Pääohjelma ######

kilpailu = Kilpailu("Suuri romuralli", 8000, 10)

while Kilpailu.kilpailu_ohi == True:

	for tunti in range(11):
		kilpailu.tunti_kuluu()
	
	Kilpailu.tulosta_tilanne
	Kilpailu.kilpailu_ohi()

kilpailu.tulosta_tilanne()