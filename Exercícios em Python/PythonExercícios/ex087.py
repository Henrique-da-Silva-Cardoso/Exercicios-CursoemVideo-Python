matriz = [[], [], []]
par = somater = 0
for c in range(0, 9):
    num = int(input(f'Digite um valor para [{c//3}, {c%3}]: '))
    if num % 2 == 0:
        par += num
    if c < 3:
        matriz[0].append(num)
    elif c < 6:
        matriz[1].append(num)
    else:
        matriz[2].append(num)

print('-='*40)
for p in matriz:
    print(f'[{p[0]:^5}][{p[1]:^5}][{p[2]:^5}]')
    somater += p[2]
print('-='*40)

print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {somater}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')
