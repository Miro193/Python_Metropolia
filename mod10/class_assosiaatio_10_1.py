# Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron. 
# Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa. 
# Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5), 
# metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen. 
# Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on. 
# Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

class Hissi:
	def __init__(self, alin, ylin):
		self.alin = alin
		self.ylin = ylin
		self.nykyinen_kerros = alin

	def siirry_kerrokseen(self, kerros):
		if kerros > self.ylin or kerros < self.alin: # kerrosten vertailu
			print(f"Kerrosta ei löydy.")
			return
		while kerros > self.nykyinen_kerros:
				self.kerros_ylos()
		while kerros < self.nykyinen_kerros:
				self.kerros_alas()

	def kerros_ylos(self):
		self.nykyinen_kerros += 1
		print(f"Kerros: {self.nykyinen_kerros}")

	def kerros_alas(self):
		self.nykyinen_kerros -= 1
		print(f"Kerros: {self.nykyinen_kerros}")

	
uusi_hissi = Hissi(1,9)
# print(vars(uusi_hissi))
uusi_hissi.siirry_kerrokseen(5)
# print(vars(uusi_hissi))