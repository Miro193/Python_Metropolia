# Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
# Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen
# ilmoittaen samalla käyttäjälle, montako senttiä alimmasta sallitusta
# pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on alle 37 cm.

kalan_pituus = float(input("Anna kuhan pituus cm:nä: "))
# alamitta = 37 - kalan_pituus

if kalan_pituus >= 37:
    print("Kuhan pituus on täysimittainen ja laillinen.")

else:
    alamitta = 37 - kalan_pituus
    print(f"Kuha on {alamitta:.2f}cm alamittainen, laske kuha takaisin veteen!")
