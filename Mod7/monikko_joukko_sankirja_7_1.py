# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka
#  jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
#  Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
#  Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten,
#  että joulukuu on ensimmäinen talvikuukausi.

def vuodenajat(i):
	vuodenajat = ('talvi', 'kevät', 'kesä', 'syksy')

	if i == 12 or i == 1 or i == 2:
		return vuodenajat[0] # talvi
	elif i == 3 or i == 4 or i ==5:
		return vuodenajat[1] # kevät
	elif i == 6 or i == 7 or i == 8:
		return vuodenajat[2] # kesä
	elif i == 9 or i == 10 or i== 11:
		return vuodenajat[3] # syksy


luku = int(input('Anna kuukauden järjestysnumero (1-12): '))
kuukausi = vuodenajat(luku)
print(kuukausi)
