""" Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador 
vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer."""

from random import randint
computador = randint(0, 10)
print("Sou seu computador... Acabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adinhar qual foi? ")
acertou = False
while not acertou:
   jogador = int(input("Qual é seu palpite? "))
   if jogador == computador:
      acertou  = True
print("Acertou!")