pessoas = []
dados = []
cont = kgleve = kgpes = 0
leve = []
pesado = []
while True:
    dados.append(str(input('Nome: ')).strip())
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        kgleve = dados[1]
        kgpes = dados[1]
    elif dados[1] > kgpes:
        kgpes = dados[1]
    elif dados[1] < kgleve:
        kgleve = dados[1]
    pessoas.append(dados[:])
    cont += 1
    dados.clear()
    esc = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    if esc in 'Nn':
        break
for p in pessoas:
    if p[1] == kgleve:
        leve.append(p[0])
    elif p[1] == kgpes:
        pesado.append(p[0])
print('-'*40)
print(f'Foram cadastradas {cont} pessoas')
print(f'O maior peso foi de {kgpes}kg. Peso de {pesado}')
print(f'O menor peso foi de {kgleve}kg. Peso de {leve}')
