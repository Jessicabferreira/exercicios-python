"""
Faça um programa que leia o comprimento do cateto opsto e do cateto adjacente de um triangulo. Calcule e mostre o
comprimento da hipotenusa.
"""

# Exemplo 1
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))
print()

# Exemplo 2 método importado
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

