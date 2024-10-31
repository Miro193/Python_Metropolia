
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