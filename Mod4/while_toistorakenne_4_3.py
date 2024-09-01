# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

luku = input('Anna luku: ')
pienin = luku
suurin = 0

while luku != "":

    if int(luku) > suurin:
        suurin = int(luku)

    elif int(luku) < int(pienin):
        pienin = int(luku)

    luku = input('Anna luku: ')

print(f"suurin numero on {suurin}")
print(f"pienin pienin on {pienin}")