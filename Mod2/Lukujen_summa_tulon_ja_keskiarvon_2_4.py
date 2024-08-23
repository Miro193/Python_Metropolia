# Lukujen summan, tulon ja keskiarvon

luku_1 = int(input("Anna ensimmäinen kokonaisluku: "))
luku_2 = int(input("Anna toinen kokonaisluku: "))
luku_3 = int(input("Anna kolmas kokonaisluku: "))

summa = luku_1 + luku_2 + luku_3
tulo = luku_1 * luku_2 * luku_3
keskiarvo = summa / 3

print(f"Lukujen summa on: {summa}")
print(f"Lukujen tulo on: {tulo}")
print(f"Lukujen keskiarvo on: {keskiarvo:.1f}")