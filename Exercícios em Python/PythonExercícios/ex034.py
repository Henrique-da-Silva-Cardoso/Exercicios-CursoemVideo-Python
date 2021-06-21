sal = float(input('Digite seu salário: '))

if sal > 1250:
    print(f'Seu aumento foi de 10%, seu salário foi de \033[33m{sal}\033[m para \033[31m{sal + sal*0.1}')
else:
    print(f'Seu aumento foi de 15%, seu salário foi de \033[33m{sal}\033[m para \033[32m{sal + sal*0.15}')
