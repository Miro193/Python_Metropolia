# Arpoo ja tulostaa kaksi erilaista numerolukon koodia.
# Ensimmäinen on 3 numeroinen ja toinen on nelinumeroinen.
# mod 2.6

from random import randint

print(f"kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9:\n{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}")
print(f"Nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9:\n{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}")
