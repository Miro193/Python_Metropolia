# Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto. 
# Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina. Polttomoottoriauton ominaisuutena 
# on bensatankin koko litroina. Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa 
# parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin. Se kutsuu yliluokan alustajaa 
# kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa. 
# Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden 
# polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). Aseta kummallekin autolle haluamasi nopeus, 
# käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.

from auto import Auto


class Sahkoauto(Auto):
	def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti_kWh):
		super().__init__(rekisteritunnus, huippunopeus)
		self.akkukapasiteetti_kWh = akkukapasiteetti_kWh

class Polttomoottoriauto(Auto):
	def __init__(self, rekisteritunnus, huippunopeus, bensatankki_l):
		super().__init__(rekisteritunnus, huippunopeus)
		self.bensatankki_l = bensatankki_l

# --------- Pääohjelma -------------------#

if __name__ == "__main__":

	uusi_auto = []
	uusi_auto.append(Sahkoauto("ABC-15", 180 , 52.5))
	uusi_auto.append(Polttomoottoriauto("ACD-123", 165, 32.3))

	uusi_auto[0].kiihdytaa(122)
	uusi_auto[1].kiihdytaa(141)

	for a in range(len(uusi_auto)):
		uusi_auto[a].kulje(3)

	for b in uusi_auto:
		print(f"Tunnuksella: {b.rekisteritunnus}, auton matkamittarilukema on:  {b.kuljettu_matka} km.")