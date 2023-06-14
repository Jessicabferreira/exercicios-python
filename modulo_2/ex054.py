"""  Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
 ainda não atingiram a maioridade e quantas já são maiores.
"""
from datetime import date
atual = date.today().year
nasc = int(input("Em que ano a pessoa nasceu? "))
idade = atual - nasc
print("Essa pessoa tem {} anos".format(idade))
