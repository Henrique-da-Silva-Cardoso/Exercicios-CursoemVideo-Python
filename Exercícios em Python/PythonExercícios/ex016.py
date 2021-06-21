'''from math import trunc

num = float(input('Insira um número com casas decimais: '))

print(f'O número {num} só com sua parte inteira é {trunc(num)}')'''

num = float(input('\033[4mInsira um número com casas decimais:\033[m '))
print(f'O número \033[36m{num}\033[m só com sua parte inteira é \033[37m{int(num)}\033[m')