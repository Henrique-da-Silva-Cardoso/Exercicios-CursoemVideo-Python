print('-'*40)
jogadores = []
while True:
    jog = {'nome': input('Nome do Jogador: ')}
    partidas = int(input(f'Quantas partidas {jog["nome"]} jogou? '))
    jog['gols'] = 0
    jog['total'] = 0
    for c in range(0, partidas):
        if c == 0:
            jog['gols'] = []
        gol = int(input(f'Quantos gols na partida {c+1}? '))
        jog['gols'].append(gol)
        jog['total'] += gol
    jogadores.append(jog)

    esc = input('Quer inserir mais um? [S/N]: ')
    if esc in 'Nn':
        print('-='*20)
        break
    print('-'*40)

print('''
 cod  nome                 gols                    total
------------------------------------------------------------''')
for c in range(0, len(jogadores)):
    print(f'{c:>5} {jogadores[c]["nome"]:<20} {str(jogadores[c]["gols"]):<23}   {jogadores[c]["total"]:^3}')

while True:
    esc = int(input('Mostrar dados de qual jogador? (negativo para parar): '))
    while esc > len(jogadores):
        esc = int(input(f'ERRO! Não existe jogador com código {esc}! Tente novamente: '))

    if esc < 0:
        print('<<<VOLTE SEMPRE>>>')
        break

    print(f'--LEVANTAMENTO DO JOGADOR {jogadores[esc]["nome"].upper()}:')
    for c in range(0, len(jogadores[esc]['gols'])):
        print(f'    No jogo {c+1} fez {jogadores[esc]["gols"][c]} {"gol" if jogadores[esc]["gols"][c] == 1 else "gols"}')

