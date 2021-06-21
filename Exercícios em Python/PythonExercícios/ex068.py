from random import randint
from time import sleep
print('\033[33m=-='*15)
print(f'{"PAR OU ÍMPAR":^40}')
print('\033[33m=-='*15 + '\033[m')
cont, esc = 0, ' '
while esc not in 'Nn':
    while True:
        escolha = int(input('Digite um valor entre 1 e 5: '))
        while escolha < 0 or escolha > 5:
            escolha = int(input('Você não tem tantos dedos assim! Rejogue: '))

        jogador = str(input('Você quer PAR [P] ou ÍMPAR [I]? ')).strip()[0]
        while jogador not in 'PpIi':
            jogador = str(input('Valor inválido, digite novamente [P/I]: ')).strip()[0]

        print('Estou pensando em um número, espere um momento...')
        num = randint(1, 5)
        sleep(2)
        print('PENSEI!')
        sleep(1.5)
        print('Agora vejamos se você ganhou ou perdeu. ')
        sleep(2)
        soma = escolha + num

        if jogador in 'Pp':
            if soma % 2 == 0:
                print(f'Você ganhou, a soma {soma} era par, vamos ver quantas mais vezes você conseguirá...')
                cont += 1
            else:
                print(f'Você perdeu, a soma {soma} não era par, parece que a sorte não estava ao seu lado.')
                break
        elif jogador in 'Ii':
            if soma % 2 != 0:
                print(f'Você ganhou, a soma {soma} era ímpar, vamos ver quantas mais vezes você conseguirá...')
                cont += 1
            else:
                print(f'Você perdeu, a soma {soma} não era ímpar, parece que a sorte não estava ao seu lado.')
                break
    sleep(2)
    print(f'Você conseguiu ganhar {cont} vezes!')
    if cont == 0:
        print('Infelizmente.')
    elif 0 < cont <= 3:
        print('Você é um pouco sortudo.')
    elif 3 < cont <= 6:
        print('Você é bem sortudo!')
    elif 6 < cont <= 10:
        print('Você é muito sortudo!')
    elif 10 < cont:
        print('Você é esplendorosamente sortudo! Deverias jogar na mega sena!')
    esc = ' '
    while esc not in 'SsNn':
        esc = str(input('Quer tentar denovo? [S/N]: ')).strip()[0]
print('Obrigado por utilizar o programa PAR OU ÍMPAR, volte sempre!')
