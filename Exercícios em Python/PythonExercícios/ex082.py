valores = []
par = []
impar = []
while True:
    valores.append(int(input('Digite um valor: ')))
    esc = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    while esc not in 'SsNn':
        esc = str(input('Comando inválido digite novamente [S/N]: ')).strip()[0]
    if esc in 'Nn':
        break

for valor in valores:
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)

print(f'''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
A lista de todos os valores digitados é {valores}
Desses os números pares digitados foram {par}
E os números ímpares digitados foram {impar}
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
