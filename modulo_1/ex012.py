# Faça um programa que leia o preço de um produdo e mostre seu novo preço, com 5% de desconto.

preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 5/ 100)
print('O produto que custava {:.2f}, na promoção com desconto de 5% vai custar {:.2f}'.format(preço, novo))

