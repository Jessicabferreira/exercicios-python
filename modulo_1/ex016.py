"""
 Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
"""

# Exemplo 1
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a porção inteira é {}'.format(num, int(num)))
print()

# Exemplo 2 com módulo importado
from math import trunc

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))

