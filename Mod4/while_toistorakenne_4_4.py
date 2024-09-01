# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

from random import randint

luku = randint(1, 10)
vastaus = "Oikein!"
arvaus = int(input("Arvaa mikä numero 1-10:"))

if luku == arvaus:
	print(vastaus)

else:
	while luku != arvaus:

		if luku > arvaus:
			print(f"Arvaus liian pieni!")
			arvaus = int(input("Arvaa uusi numero 1-10:"))

		elif luku < arvaus:
			print(f"Arvaus liian suuri!")
			arvaus = int(input("Arvaa uusi numero 1-10:"))

	print(vastaus)