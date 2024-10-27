# Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
#  Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
#  Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
#  Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
#  Asenna kirjasto valitsemalla View / Tool Windows / Python Packages.
#  Kirjoita hakukenttään geopy ja vie asennus loppuun.

import geopy.distance
import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True
         )

def hae_lentoketta_icao_koodilla(koodi):
    sql = f"SELECT name, latitude_deg, longitude_deg FROM airport WHERE ident LIKE %s;"
    # print(sql)
    kursori = yhteys.cursor() #dictionary=True
    kursori.execute(sql, (koodi,))
    return kursori.fetchall()

# Testattu EFHK , 00A, 00AA ja 00CO icao koodilla ainakin.

icao_koodi_1 = input('Anna ensimmäisen lentokentän ICAO-koodi:')
icao_koodi_2 = input('Anna toisen lentokentän ICAO-koodi:')

kordinaatit_1 = hae_lentoketta_icao_koodilla(icao_koodi_1)
kordinaatit_2 = hae_lentoketta_icao_koodilla(icao_koodi_2)
print(kordinaatit_1)
print(kordinaatit_2)

if kordinaatit_1 is not None and len(kordinaatit_1) > 0 and kordinaatit_2 is not None and len(kordinaatit_2) > 0:
    lentokentta_1 = kordinaatit_1[0][0]
    lentokentta_2 = kordinaatit_2[0][0]
    paikka_1 = [kordinaatit_1[0][1], kordinaatit_1[0][2]]
    paikka_2 = [kordinaatit_2[0][1], kordinaatit_2[0][2]]
    print(f'Lentokenttien {lentokentta_1} ja {lentokentta_2} etäisyys toisistaan on {geopy.distance.geodesic(paikka_1, paikka_2).km:.2f} km.')

else:
    print('Koodit väärin, lentokenttiä ei löytynyt')
