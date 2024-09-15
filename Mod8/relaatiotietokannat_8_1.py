# Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin. Ohjelma hakee ja tulostaa
#  koodia vastaavan lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä
#  lentokenttätietokannasta. ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.

import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True
         )

def hae_lentoketta_icao_koodilla(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident = %s"
    # print(sql)
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, (icao,))
    return kursori.fetchone()

koodi = input('Syötä lentokentän ICAO koodi: ')
lentokentta = hae_lentoketta_icao_koodilla(koodi)

if lentokentta is not None:
    print(f"{lentokentta['name']} on paikkakunnalla {lentokentta['municipality']}")
else:
    print('lentokenttää ei löytynyt')

