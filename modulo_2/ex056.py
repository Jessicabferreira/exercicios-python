""" Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""

somaidade = 0
médiaidade = 0
for p in range(1, 5):
    print("----- {}ª PESSOA -----".format(p))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidade += idade
    
médiaidade = somaidade / 4
print("A mádia de idade do grupo é de {} anos".format(médiaidade))
