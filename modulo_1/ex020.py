"""
O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça uma programa que
leia o nome dos quatros alunos e mostre a ordem sorteada.
"""

from random import shuffle
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
shuffle(lista)      # shuffle é embaralhar
print('A ordem de apresentação será ')
print(lista)
