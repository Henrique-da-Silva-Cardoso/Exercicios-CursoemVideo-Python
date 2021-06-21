valores = []
while True:
    num = int(input('Digite um valor: '))
    if num in valores:
        print('Duplicata, esse valor não me serve de nada!')
    else:
        valores.append(num)
        print('Valor adicionado com sucesso!')
    esc = str(input('Quer continuar? [S/N]: ')).strip()[0]
    if esc in 'Nn':
        break
valores.sort()
print('-='*40+'-')
print(f'Os números digitados foram {valores}')
