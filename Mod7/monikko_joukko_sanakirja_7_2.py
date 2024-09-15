# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä
#  syöttää tyhjän merkkijonon. Kunkin nimen syöttämisen jälkeen ohjelma tulostaa
#  joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan, syötettiinkö
#  nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan
#  allekkain mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.


nimet = {'Mikko', 'Matias'}
nimi = input('Anna nimi: ')

while nimi != '':
	if nimi not in nimet:
		print("Uusi nimi")
	elif nimi in nimet:
		print("Aiemmin syötetty nimi")

	nimet.add(nimi)
	nimi = input('Anna nimi: ')

for n in nimet:
	print(n)
# pelit = {"Monopoli", "Shakki", "Cluedo"}
# print(pelit)

# pelit.add("Dominion")
# print(pelit)

# pelit.remove("Shakki")
# print(pelit)

# pelit.add("Cluedo")
# print(pelit)

# for p in pelit:
#     print(p)