from random import randint
from time import sleep

print('\033[33m-='*29+'-\033[m')
print('Estou pensando em um número de 0 à 10, tente adivinhá-lo... ')
print('\033[33m-='*29+'-\033[m')

chute = int(input('Em que número estou pensando? '))
num = randint(0, 10)

while chute < 0 or chute > 10:
    chute = int(input('\033[1;4;31mVoce não conseguirá acertar o número se chutar acima 5 ou abaixo de 0\033[m '))

print(f'\033[3;{randint(30, 37)}mOLHA O SUSPENSE VINDO AI!\033[m')
sleep(1)

cont = 1
while chute != num:
    print(f'EU GANHEI! O número que eu pensei não era {chute} burrinho')
    if chute < num:
        chute = int(input('Tente chutar até acertar! O número anterior era muito baixo '))
    else:
        chute = int(input('Tente chutar até acertar! O número anterior era muito alto '))
    print(f'\033[3;{randint(30, 37)}mOLHA O SUSPENSE VINDO AI!\033[m')
    sleep(1)
    cont += 1

print(f'\033[4;32mVocê Ganhou! O número que eu pensei era {num} e você conseguiu acertá-lo!')
if cont == 1:
    print('Você acertou de primeira!')
else:
    print(f'Você teve que chutar {cont} vezes para acertar')
