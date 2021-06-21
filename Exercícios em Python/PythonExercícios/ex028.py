from random import randint
from time import sleep
num = randint(0, 5)

print('\033[33m-='*29+'-\033[m')
print('Estou pensando em um número de 0 à 5, tente adivinhá-lo... ')
print('\033[33m-='*29+'-\033[m')

chute = int(input('Em que número estou pensando? '))

while chute < 0 or chute > 5:
    chute = int(input('\033[1;4;31mVoce não conseguirá acertar o número se chutar acima 5 ou abaixo de 0\033[m '))

print('OLHA O SUSPENSE VINDO AI!')
sleep(2)

if chute == num:
    print(f'Você Ganhou! O número que eu pensei era {num} e você conseguiu acertá-lo!')
else:
    print(f'EU GANHEI! O número que eu pensei era {num} e não {chute} burrinho')
