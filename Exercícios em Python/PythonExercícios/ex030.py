num = int(input('Digite um número: '))

print(f'O número \033[1;34m{num}\033[m é PAR' if num % 2 == 0 else f'O número \033[1;31m{num}\033[m é ÍMPAR')
