jog = {'nome': input('Nome do Jogador: '), 'gols': 0, 'total': 0}
partidas = int(input(f'Quantas partidas {jog["nome"]} jogou? '))
for c in range(0, partidas):
    if c == 0:
        jog['gols'] = []
    gol = int(input(f'Quantos gols na partida {c+1}? '))
    jog['gols'].append(gol)
    jog['total'] += gol
print('-='*30)
print(jog)
print('-='*30)
for k, v in jog.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jog["nome"]} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'    => Na partida {c+1}, fez {jog["gols"][c]} {"gol" if jog["gols"][c] == 1 else "gols"}.')
print(f'Foi um total de {jog["total"]} gols.')
