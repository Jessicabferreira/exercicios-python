"""Faça um programa que leia um número qualquer e mostre o seu fatorial
Exemplo:  5!= 5x4x3x2x1= 120"""

n = int(input("Digite um número para calcular seu Fatorial: "))
c = n
while c > 0:
    print("{} x ".format(c), end=' ')
    c -= 1
# print("O fatorial de {} é {}.".format(n, f))
