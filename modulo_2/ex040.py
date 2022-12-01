"""
 Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem
 no final, de acordo com a média atingida:
"""
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))

if media >= 5 and media < 7:
    print('O aluno está de RECUPERAÇÂO'.format(media))
elif media >= 7:
    print('O aluno foi APROVADO'.format(media))
else:
    print('O aluno foi REPROVADO'.format(media))
