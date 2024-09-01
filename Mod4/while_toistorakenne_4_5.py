# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
# (Oikea käyttäjätunnus on python ja salasana rules).

oikea_kayttajatunnus = "python"
oikea_salasana = "rules"

kayttajatunnus = ''
salasana = ''
laskuri = 0
vastaus = 'Tervetuloa'

while laskuri < 5:

	kayttajatunnus = input('Anna käyttäjätunnus:')
	salasana = input('Anna salasana: ')

	if (kayttajatunnus == oikea_kayttajatunnus and salasana == oikea_salasana) and laskuri < 5:
		vastaus = 'Tervetuloa'
		break

	else:
		vastaus = 'Pääsy evätty'

	laskuri += 1
print(vastaus)