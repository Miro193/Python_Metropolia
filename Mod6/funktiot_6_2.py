# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän. 
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. 
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes 
# saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.

from random import randint

def nopan_tahko(maara):
	tahko = randint(1, maara)
	return tahko

kutsu = int(input('Anna nopan tahkojen määrä: '))
tahko = 0

while kutsu != tahko:
	tahko = nopan_tahko(kutsu)
	print(tahko)

