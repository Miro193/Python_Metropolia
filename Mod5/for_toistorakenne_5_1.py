# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
# Käytä for-toistorakennetta.

from random import randint

heitot = int(input('Monta arpakuutiota: '))

# arpakuutiot = []
summa = 0
for i in range(heitot):
	kuutio = randint(1, 6)
	summa += kuutio
print(summa)
