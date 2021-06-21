from time import sleep
num = int(input('Digite um número inteiro qualquer: '))
opt = int(input('''Escolha para que base esse número irá ser convertido
    \033[31m[ 1 ]\033[m Para converter para binário
    \033[33m{ 2 }\033[m Para converter para octal
    \033[34m( 3 )\033[m Para converter para hexadecimal
                    '''))

if opt == 1:
    print('A base escolhida foi \033[1;30mbinário\033[m')
    print('\033[36mAnalisando o número, espere um pouco...\033[m')
    sleep(2)
    print(f'{num} em binário é {bin(num)[2:]}')
elif opt == 2:
    print('A base escolhida foi \033[4;35moctal\033[m')
    print('\033[36mAnalisando o número, espere um pouco...')
    sleep(2)
    print(f'{num} em binário é {oct(num)[2:]}')
elif opt == 3:
    print('A base escolhida foi \033[7;33mhexadecimal\033[m')
    print('\033[36mAnalisando o número, espere um pouco...')
    sleep(2)
    print(f'{num} em binário é {hex(num)[2:]}')
else:
    print('O número digitado não é válido, por favor reinicie o programa')
