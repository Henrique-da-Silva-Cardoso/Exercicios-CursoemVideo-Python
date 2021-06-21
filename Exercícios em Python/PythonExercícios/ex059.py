from time import sleep
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))

opt = 0
while opt != 5:
    opt = int(input(
        '''\033[33m====== DIGITE ======
|\033[m \033[1;33m    [1]SOMAR\033[m     \033[33m|
|\033[m \033[1;34m [2]MULTIPLICAR\033[m  \033[33m|
|\033[m \033[1;35m    [3]MAIOR\033[m     \033[33m|
|\033[m \033[1;36m[4]NOVOS NÚMEROS\033[m \033[33m|
|\033[m     \033[1;30;41m [5]SAIR \033[m    \033[33m|
====================\033[m
          '''))
    while opt < 1 or opt > 5:
        opt = int(input('Valor inválido, digite novamente: '))

    if opt == 1:
        print(f'A soma dos números {n1} e {n2} é {n1+n2}')
    elif opt == 2:
        print(f'A multiplicação dos número {n1} e {n2} é {n1*n2}')
    elif opt == 3:
        if n1 > n2:
            print(f'Dentre os números {n1} e {n2}, {n1} é o maior')
        elif n1 < n2:
            print(f'Dentre os números {n1} e {n2}, {n2} é o maior')
        elif n1 == n2:
            print(f'Os dois números são iguais')
    elif opt == 4:
        n1 = int(input('Digite o valor que você deseja que substitua o primeiro anterior: '))
        n2 = int(input('Digite o valor que você deseja que substitua o segundo anterior: '))

    if opt != 5:
        print('Voltando para o menu...')
        sleep(2)
    else:
        print('\033[4mSaindo do programa...')
        sleep(2)