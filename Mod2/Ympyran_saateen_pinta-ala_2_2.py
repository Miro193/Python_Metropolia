# Ohjelma kysyy ympyrän säteen ja tulostaa sen pinta-alan.
# mod 2.2
import math

sade = int(input("Anna ympyrän säde senttimetreinä: "))
pinta_ala = math.pi*(sade**2)
print(f"Ympyrän pinta-ala on:\n{pinta_ala:.1f} cm^2.")
