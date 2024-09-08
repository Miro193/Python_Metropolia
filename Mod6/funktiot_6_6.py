# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä
#  pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri. 
#  Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza
#  antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta). Yksikköhintojen laskennassa
#  on hyödynnettävä kirjoitettua funktiota.

def koko_hinta_keskiarvo(koko, hinta):
	pizzan_sade_cm = koko / 2
	pizza_cm2 = 3.14 * pizzan_sade_cm**2
	pizza_m2 = pizza_cm2 / 10000
	euro_m2 = pizza_m2 * hinta
	return euro_m2

# Ekan pizzan kysely
pizza1_halkaisija = float(input('Anna ensimmäisen pizzan halkaisija cm: '))
pizza1_hinta = float(input('Anna ensimmäisen pizzan hinta euroina: '))
pizza1 = koko_hinta_keskiarvo(pizza1_halkaisija, pizza1_hinta)
# print(f'pizzan hinta on {pizza1:.3} €/m^2')

# tokan pizzan kysely
pizza2_halkaisija = float(input('Anna toisen pizzan halkaisija cm: '))
pizza2_hinta = float(input('Anna toisen pizzan hinta euroina: '))
pizza2 = koko_hinta_keskiarvo(pizza2_halkaisija, pizza2_hinta)
# print(f'pizzan hinta on {pizza2:.3} €/m^2')

if pizza1 > pizza2:
	print('Pizza 1 antaa enemmän rahalle vastinetta. Pizzan hinta on {pizza2:.3} €/m^2')
elif pizza1 < pizza2:
	print('Pizza 2 antaa enemmän rahalle vastinetta. Pizzan hinta on {pizza2:.3} €/m^2')
else:
	print('Pizzat Antavat saman vastineen rahoillesi.')
