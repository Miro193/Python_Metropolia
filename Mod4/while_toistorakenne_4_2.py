# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä
# antaa negatiivisen tuumamäärän. Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

tuuma = float(input("Tuuma: "))

while tuuma > 0:
    tuuma_senteiksi = float(tuuma * 2.54)
    print(tuuma_senteiksi)
    tuuma = float(input("Tuuma: "))