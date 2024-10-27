# Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina annetaan alimman ja 
# ylimmän kerroksen numero sekä hissien lukumäärä. Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. 
# Hissien lista tallennetaan talon ominaisuutena. Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen. 
# Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

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
		print(f"Valitsitte hissin: {hissin_num}")
		self.hissit[hissin_num -1].siirry_kerrokseen(kohdekerros)
		
		# else:
		# 	print(f"Valitsitte hissin: {vars(self.hissit[hissin_num -1])}")
		# 	self.hissit[hissin_num -1].siirry_kerrokseen(kohdekerros)

# uusi_talo = Talo(1, 10, 3)

# uusi_talo.aja_hissia(2, 9)
# uusi_talo.aja_hissia(4, 10)
# uusi_talo.aja_hissia(3, 14)
# uusi_talo.aja_hissia(3, 10)
