tot = [[], []]
print(f'{"Par ou Ímpar":=^40}')
for c in range(0, 7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        tot[0].append(num)
    else:
        tot[1].append(num)
print('-'*40)
tot[0].sort()
tot[1].sort()
print(f'Os valores pares digitados foram: {tot[0]}')
print(f'Os valores ímpares digitados foram: {tot[1]}')
