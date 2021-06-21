from random import randint
from time import sleep

print('-'*40)
print(f'{"JOGUE NA MEGA SENA":^40}')
print('-'*40)

vezes = int(input('Quantos jogos você quer que eu sorteie? '))
sena = []
jogo = []
print(f'{f" SORTEANDO OS {vezes} JOGOS ":=^40}')

for jogos in range(0, vezes):
    for chutes in range(0, 6):
        num = randint(1, 60)
        while num in jogo:
            num = randint(1, 60)
        jogo.append(num)
    sena.append(jogo[:])
    jogo.clear()
    sena[jogos].sort()
    print(f'Jogo {jogos+1:>3}: {sena[jogos]}')
    sleep(0.75)

print('-='*6, '< BOA SORTE! >', '=-'*6)
