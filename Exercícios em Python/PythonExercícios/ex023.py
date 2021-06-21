num = int(input('Escreva um número de 0 à 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'unidade: \033[33m{u}\033[m')
print(f'dezena: \033[33m{d}\033[m')
print(f'centena: \033[33m{c}\033[m')
print(f'milhar: \033[33m{m}\033[m')
