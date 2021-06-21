from random import choice, randint
import emoji
from time import sleep
print('\033[33m-\033[m'*60)
print('                     \033[35mVamos jogar jo-ken-po?\033[m')
print('\033[33m-\033[m'*60)

opt = ['pedra', 'papel', 'tesoura']
opt = choice(opt)

mao = str(input(f'Escolha dentre as três opções {emoji.emojize(":volcano:")} pedra, '
                f'{emoji.emojize(":page_facing_up:")} papel e '
                f'{emoji.emojize(":scissors:")} tesoura '
                f'\n                              ')).strip().lower()

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')

print('='+'-='*10)
print(f'\033[4;{randint(31,33)}mVocê escolheu {mao}')
if mao == opt:
    sleep(1)
    print(f'\033[4;{randint(31, 33)}mEu escolhi {opt.title()+"."}\033[m')
    print('=' + '-=' * 10)

    print(f'\033[4;{randint(31, 33)}mNós Empatamos.')
elif mao == 'papel':
    sleep(1)
    if opt == 'pedra':
        print(f'\033[4;{randint(31, 33)}mEu escolhi {opt.lower()+"..."}\033[m')
        print('=' + '-=' * 10)

        print(f'\033[4;{randint(31, 33)}mEu perdi, parabéns!')
    elif opt == 'tesoura':
        print(f'\033[4;{randint(31, 33)}mEu escolhi {opt.upper() + "!"}\033[m')
        print('=' + '-=' * 10)

        print(f'\033[4;{randint(31, 33)}mEu venci, toma essa!')
elif mao == 'pedra':
    sleep(1)
    if opt == 'papel':
        print(f'\033[4;{randint(31, 33)}mEu escolhi {opt.upper()+"!"}\033[m')
        print('=' + '-=' * 10)

        print(f'\033[4;{randint(31, 33)}mEu venci, toma essa!')
    else:
        print(f'\033[4;{randint(31, 33)}mEu escolhi {opt.lower()+"..."}\033[m')
        print('=' + '-=' * 10)

        print(f'\033[4;{randint(31, 33)}mEu perdi, parabéns!')
elif mao == 'tesoura':
    sleep(1)
    if opt == 'papel':
        print(f'\033[4;{randint(31, 33)}mEu escolhi {opt.lower()+"..."}\033[m')
        print('=' + '-=' * 10)

        print(f'\033[4;{randint(31, 33)}mEu perdi, parabéns!')
    elif opt == 'pedra':
        print(f'\033[4;{randint(31, 33)}mEu escolhi {opt.upper()+"!"}\033[m')
        print('=' + '-=' * 10)

        print(f'\033[4;{randint(31, 33)}mEu venci, toma essa!')
else:
    print('Valor inserido inválido, reinicie o programa.')
