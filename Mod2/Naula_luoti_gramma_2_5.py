# Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan
# leivisköinä, nauloina ja luoteina. Ohjelma muuntaa syötteen täysiksi kilogrammoiksi
# ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

leiviskat = float(input("Anna leiviskät. "))
naulat = float(input("Anna naulat. "))
luodit = float(input("Anna luodit. "))

luodit_g = 13.3
naulat_g = luodit_g * 32
leiviskat_g = naulat_g * 20

leiviskat_paino = leiviskat * leiviskat_g
naulat_paino = naulat * naulat_g
luodit_paino = luodit * luodit_g
koko_paino = leiviskat_paino + naulat_paino + luodit_paino
kilot = int(koko_paino // 1000)
grammat = koko_paino % 1000

print(f"Massa nykymittojen mukaan:\n{kilot} kilogrammaa ja {grammat:.2f} grammaa.")