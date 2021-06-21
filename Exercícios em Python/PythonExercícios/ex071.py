print('\033[34m-=-'*15)
print(f'{"CAIXA ELETRÔNICO":^45}')
print('-=-'*15 + '\033[m')
notas = [0, 0, 0, 0, 0, 0]
valor = (100, 50, 20, 10, 2, 1)
while True:
    num = int(input('Preço: R$'))
    if num >= 100:
        notas[0] = num // 100
        num -= 100 * notas[0]
    if num >= 50:
        notas[1] = num // 50
        num -= 50 * notas[1]
    if num >= 20:
        notas[2] = num // 20
        num -= 20 * notas[2]
    if num >= 10:
        notas[3] = num // 10
        num -= 10 * notas[3]
    if num >= 2:
        notas[4] = num // 2
        num -= 2 * notas[4]
    if num >= 1:
        notas[5] = num // 1
        num -= 1 * notas[5]

    for cont in range(0, len(valor)):
        if notas[cont] != 0:
            print(f'{notas[cont]} de R${valor[cont]}')

    esc = str(input('Deseja sair do programa? [S/N]: ')).strip()[0]
    if esc in 'Ss':
        break

print('Obrigado por utilizar o programa Caixa Registradora, volte sempre!')
'''

print('\033[34m-=-'*15)
print(f'{"CAIXA ELETRÔNICO":^45}')
print('-=-'*15 + '\033[m')
esc = 'S'
valor, ced, totced = 0, 0, 0
while True:
    if esc in 'Ss':
        valor = int(input('Digite o valor a ser sacado: R$'))
        ced = 50
        totced = 0
    else:
        break

    while valor != 0:
        while valor >= ced:
            valor -= ced
            totced += 1
        else:
            if totced > 0:
                print(f'Total de {totced} cédulas de R${ced}')
            if ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 1
            totced = 0

    esc = ' '
    while esc not in 'SsNn':
        esc = str(input('Valor inválido, digite novamente [S/N]: ')).strip()[0]

print('Obrigado por utilizar o programa CAIXA ELETRÔNICO, volte sempre!')'''
