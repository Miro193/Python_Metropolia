# Ohjelma tulostaa suorakulmion piirin ja pinta-alan.

kanta = int(input("Anna suorakulmion kanta cm: "))
pituus = int(input("Anna suorakulmion korkeus cm: "))

pinta_ala = kanta * pituus
piiri = kanta * 2 + pituus * 2

print(f"Pinta-ala on: {pinta_ala:.2f}cm^2\nPiiri on: {piiri:.2f}cm")