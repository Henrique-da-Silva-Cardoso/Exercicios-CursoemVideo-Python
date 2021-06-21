media = 0
i = 'S'
cont = 0
maior = 0
menor = 0
while i in 'Ss':
    num = float(input('Digite um valor: '))
    if cont == 0:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    media += num
    cont += 1
    i = str(input('Quer continuar? [S/N]: ')).strip()[0]
print(f'A média de todos os {cont} números foi {media/cont}, o maior número foi {maior} e o menor foi {menor}')
