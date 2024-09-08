# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen 
# nopan silmäluvun väliltä 1..6. Kirjoita pääohjelma, joka heittää noppaa niin 
# kauan kunnes tulee kuutonen. Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

from random import randint

def nopan_heitto():
	heitto = randint(1, 6)
	return heitto

numero = 0

while numero != 6:
	numero = nopan_heitto()
	print(numero)
