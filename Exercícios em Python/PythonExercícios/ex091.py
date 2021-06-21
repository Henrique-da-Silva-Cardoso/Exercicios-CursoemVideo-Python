from random import randint
from time import sleep
# from operator import itemgetter
cont = 1
jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}

for jog, num in jogadores.items():
    print(f'O {jog} tirou {num}')
    sleep(0.75)

print('Ranking dos Jogadores: ')
#ranking = sorted(jogadores.items(), itemgetter(1), reverse=True)
#print(ranking)
#for i, v in enumerate(ranking):
#   print(f'{i} lugar: {v[0]} com {v[1]}.')
#   sleep(1)
for jog, num in sorted(jogadores.items(), key=lambda x: x[1], reverse=True):
    print(f'{cont}° lugar: {jog} com {num}')
    cont += 1
    sleep(0.75)
