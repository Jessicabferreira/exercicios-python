"""
Faça um programa que leia uma frase pelo teclado e mostre:
quantas vezes aparece a letra "A".
em que posição ela aparece a primeira vez.
Em que posição ela aparece a última vez.
"""

frase = str(input('Digite uma frase: ')).upper().strip()   # upper vai pra maiuscula/ strip tira espaços indesejados
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))    # count vai mostrar a qnt de letras A
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))  # find+1 começa a contar apartir de 1
print('A  última letra A apareceu na posição {}'.format(frase.rfind('A')+1))  # rfind procure apartir do lado direito