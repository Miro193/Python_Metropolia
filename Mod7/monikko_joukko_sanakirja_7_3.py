# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
#  Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman,
#  hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee
#  uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
#  Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä
#  vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
#  Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti,
#  kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste.
#  Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)


def hae(asema_tiedot):
    koodi = input("Syötä ICAO-koodi: ")
    if koodi in asema_tiedot:
        print(asema_tiedot[koodi])
    else:
        print("Ei löydy koodia tai asemaa.")
 
def lisaa(asema_tidot):
    koodi = input("Anna ICAO-koodi: ")
    nimi = input("Aseman nimi: ")
    asema_tiedot[koodi] = nimi
    print("Ok!")
 

asema_tiedot = {}

while True:
	komento = input("Haluatko (1 lisätä uuden aseman, 2 hakea jo syötetyn aseman, 3 lopeta)? ")
	if komento == "1":
		lisaa(asema_tiedot)
	if komento == "2":
		hae(asema_tiedot)
	if komento == "3":
		break
    
print("lopetetaan...")