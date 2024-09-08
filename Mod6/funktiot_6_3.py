# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina 
# ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, 
# joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. 
# Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka, 
# kunnes käyttäjä syöttää negatiivisen gallonamäärän.
# Yksi gallona on 3,785 litraa.

def gallona_litroiksi(maara):
	litra = 3.785
	maara *= litra
	return maara

gallona = float(input('Anna bensiinin määrä gallonoina: '))

while gallona > 0:
	print(f"{gallona_litroiksi(gallona)} litraa")
	gallona = float(input('Anna bensiinin määrä gallonoina: '))
