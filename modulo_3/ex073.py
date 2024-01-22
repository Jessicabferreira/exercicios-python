"""
Crie uma tupla preenchida com os 20 primeiros colococados da
Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:
 
a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.
 """

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzerio', 'Flamengo', 'Vasvo', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vítória', 'Coritiba', 'avaí', 'Ponte Preta',
         'Atlético-GO')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O chapecoense está na {times.index("Chapecoense")+1}ª posicão')
