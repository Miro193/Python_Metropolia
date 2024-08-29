# Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja
# hemoglobiiniarvon (g/l). Ohjelma ilmoittaa, onko hemoglobiiniarvo
# alhainen, normaali vai korkea.

sukupuoli = input("Kumpaa sukupuolta olet (mies vai nainen):")

if sukupuoli == "mies":
    hemoglobiiniarvo = float(input("Anna hemoglobiini arvo (g/l):"))
    if hemoglobiiniarvo < 134:
        print(f'hemoglobiiniarvo {hemoglobiiniarvo}g/l miehellä on alhainen')
    elif hemoglobiiniarvo > 195:
        print(f'hemoglobiiniarvo {hemoglobiiniarvo}g/l miehellä on korkea')
    else:
        print(f'hemoglobiiniarvo {hemoglobiiniarvo}g/l miehellä on normaali')

elif sukupuoli == "nainen":
    hemoglobiiniarvo = float(input("Anna hemoglobiini arvo (g/l):"))
    if hemoglobiiniarvo < 117:
        print(f'hemoglobiiniarvo {hemoglobiiniarvo}g/l naisella on alhainen')
    elif hemoglobiiniarvo > 175:
        print(f'hemoglobiiniarvo {hemoglobiiniarvo}g/l naisella on korkea')
    else:
        print(f'hemoglobiiniarvo {hemoglobiiniarvo}g/l naisella on normaali')

else:
    print("Syötit väärän arvon!")