# Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan 
# (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen. 
# Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä kuin ne syötettiin. 
# Käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.

lista_kaupungit = []

for nimet in range(5):
	kaupungin_nimi = input('Anna kaupungin nimi: ')
	lista_kaupungit.append(kaupungin_nimi)

for kaupunki in lista_kaupungit:
	print(kaupunki)