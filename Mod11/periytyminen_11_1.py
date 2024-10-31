
# Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti. 
# Jokaisella julkaisulla on nimi. Kirjalla on lisäksi kirjoittaja ja sivumäärä, 
# kun taas lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat alustajat. 
# Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot. 
# Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua). 
# Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.
# -----------------------------------------------------------------------------------------

class Julkaisu:

	def __init__(self, nimi):
		self.nimi = nimi

class Kirja(Julkaisu):

	def __init__(self, nimi, kirjoittaja, sivumaara):
		self.kirjoittaja = kirjoittaja
		self.sivumaara = sivumaara
		super().__init__(nimi)

	def tulosta_tiedot(self):
		print(f"Kirjan nimi : {self.nimi}, kirjoittaja: {self.kirjoittaja} ja sivumäärä: {self.sivumaara}")

class Lehti(Julkaisu):

	def __init__(self, nimi, paatoimittaja):
		self.paatoimittaja = paatoimittaja
		super().__init__(nimi)

	def tulosta_tiedot(self):
		print(f"Lehti: {self.nimi}, päätoimittaja: {self.paatoimittaja}")

# ------ Pääohjelma --------- #

julkaisu = []
julkaisu.append(Lehti("Aku Ankka", "Aki Hyyppä"))
julkaisu.append(Kirja("Hytti n:o 6", "Rosa Liksom", 200))

for t in julkaisu:
    t.tulosta_tiedot()