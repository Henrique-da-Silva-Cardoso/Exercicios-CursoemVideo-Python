num = int(input('Digite o valor usado no fatorial: '))
for c in range(num, 0, -1):
    num *= c
    c -= 1
print(f'O fatorial do número inserido é {num}')
'''
from math import factorial
num = int(input('Digite o valor usado no fatorial: '))
print(f'O fatorial do núrmero {num} é {factorial(num)}')

n = int(input('Digite o valor usado no fatorial: '))
c = n
f = 1
print(f'Calculando {n}!:', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')'''