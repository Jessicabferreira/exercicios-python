"""
Como utilizar os códigos de escape sequence ANSI para configurar cores para os seus programas em Python. 
Veja como utilizar o código \033[m com todas as suas principais possibilidades.
"""

"""
Codigo: 

    \033[ 0;  33;  44m
        style text back


style = estilo do texto
0 none = sem estilo                  
1 bold = negrito                
4 underline = sublinhado                                                  
7 negative = inverte configuração


text = cor do texto
30 branco
31 vermelho
32 verde
33 amarelo
34 azul
35 magenta
36 ciano
37 cinza


back = cor do fundo
40 branco
41 vermelho
42 verde
43 amarelo
44 azul
45 magenta
46 ciano
47 cinza


"""

print('\033[31mOlá, Mundo!\033[m')  # Text vermelho
print('\033[33;45mOlá, Mundo!\033[m')  # fundo magenta
print('\033[7;33;44mOlá, Mundo!\033[m') # fundo amarelo, letra azul
print('\033[7;30mOlá, Mundo!\033[m') # fundo preto, letra cinza

""" Outra forma de usar cores"""
nome = 'Jessica'
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format('\033[4;34m', nome, '\033[m')) # nome colorido