ano = int(input('Digite um ano qualquer: '))

if ano % 4 == 0 and ano % 100 != 0 and ano % 400 == 0:
    if ano == 4:
        print(f'O ano \033[33m{ano}\033[m foi o primeiro ano bissexto!')
    else:
        print(f'O ano \033[4;32m{ano}\033[m é bissexto')
else:
    print(f'O ano \033[31m{ano}\033[m não é bissexto')
