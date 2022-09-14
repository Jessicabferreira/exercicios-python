# Faça um algoritmo que leia o salario de um funcionário e mostre seu novo salário, com 15% de aumento.

salário = float(input('Qual é o salário do funcionario? R$'))
novo = salário + (salário * 15/ 100)
print('Um funcionário que ganhava {:.2f}, com 15% de aumento, passou a receber {:.2f}'.format(salário, novo))