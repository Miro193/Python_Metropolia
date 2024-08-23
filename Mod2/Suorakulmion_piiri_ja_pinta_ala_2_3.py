# Ohjelma tulostaa suorakulmion piirin ja pinta-alan.

kanta = int(input("Anna suorakulman kanta cm: "))
pituus = int(input("Anna suorakulman korkeus cm: "))

pinta_ala = kanta * pituus
piiri = kanta + kanta + pituus + pituus

print(f"Pinta-ala on: {pinta_ala:.2f}cm^2\nPiiri on: {piiri:.2f}cm")