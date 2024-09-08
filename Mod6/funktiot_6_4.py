# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa 
# listassa olevien lukujen summan. Kirjoita testausta varten pääohjelma, jossa luot listan, 
# kutsut funktiota ja tulostat sen palauttaman summan.

def listan_summa(lista):
	summa = 0
	for numero in lista:
		summa += numero
	return summa

lukuja = []
luku = input('Anna lukuja listaan: ')
while luku != '':
	lukuja.append(int(luku))
	luku = input('Anna lukuja listaan: ')

tulos = listan_summa(lukuja)
print('Listan summa on:', tulos)