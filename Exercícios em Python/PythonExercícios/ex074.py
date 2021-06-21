from sys import maxsize
from random import randint
numeros = (randint(-maxsize, maxsize), randint(-maxsize, maxsize), randint(-maxsize, maxsize),
           randint(-maxsize, maxsize), randint(-maxsize, maxsize), )
# professor não especificou o range dos números no exercício então eu usei o maior e menor valores que podem existir no sistema
print(f'O números gerados foram:', end=' ')
for c in numeros:
        print(c, end=' ')
print(f'\nO maior número gerado foi {max(numeros)} e o menor foi {min(numeros)}')
