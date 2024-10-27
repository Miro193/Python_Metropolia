# Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys, 
# joka käskee kaikki hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys.

from class_assosiaatio_10_1 import Hissi

class Talo:
	def __init__(self, alin, ylin, lukumaara):
		self.alin = alin
		self.ylin = ylin
		self.lukumaara = lukumaara
		self.hissit = []
		for h in range(lukumaara):
			self.hissit.append(Hissi(self.alin, self.ylin))
			# print(f"hissi {h+1} luotu",vars(self.hissit[h-1]))

	def aja_hissia(self, hissin_num, kohdekerros):
		if hissin_num > self.lukumaara or hissin_num < self.alin:
			print(f"Hissiä {hissin_num} ei löydy!")
			return
		print(f"Hissi: {hissin_num}")
		self.hissit[hissin_num -1].siirry_kerrokseen(kohdekerros)

	def palohalytys(self):
		for i in range(1, self.lukumaara+1):
			
			print(f"Hissi {i} siirretään pohjakerrokseen.")
			self.hissit[i-1].siirry_kerrokseen(self.alin)


uusi_talo = Talo(1, 10, 3)

uusi_talo.aja_hissia(2, 9)
uusi_talo.aja_hissia(4, 10)
uusi_talo.aja_hissia(3, 14)
uusi_talo.aja_hissia(3, 10)

print("\n!!Hälytys!!\n")

uusi_talo.palohalytys()