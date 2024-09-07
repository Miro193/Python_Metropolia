# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää
# tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista viisi
# suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille
# argumentiksi reverse=True.

luku = input('Anna luku: ')
numerot = []

while luku != '':
	numerot.append(int(luku))
	luku = input('Anna luku: ')

numerot.sort(reverse=True)
# print(numerot)

for i in numerot[:5]:
	print(i)
