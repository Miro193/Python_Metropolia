# Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa
#  kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin. Esimerkiksi Suomen
#  osalta tuloksena on saatava tieto siitä, että pieniä lentokenttiä on 65 kappaletta, 
# helikopterikenttiä on 15 kappaletta jne.

import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True
         )

def hae_lentoketta_iso_country_koodilla(koodi):
    sql = f"SELECT COUNT(type), type FROM airport WHERE iso_country LIKE %s GROUP BY type;"
    # print(sql)
    kursori = yhteys.cursor() #dictionary=True
    kursori.execute(sql, (koodi,))
    return kursori.fetchall()

koodi = input('Syötä lentokentän maakoodi(esim. FI): ')
lentokentta = hae_lentoketta_iso_country_koodilla(koodi)
# print(lentokentta)
if lentokentta is not None and len(lentokentta) > 0:
	print(f"({koodi}) maakoodilla haettu:")
	for x in lentokentta:
		print(f"Lentokentän tyyppi: {x[1]} {x[0]}kpl.")
else:
    print('lentokenttää ei löytynyt')
		

