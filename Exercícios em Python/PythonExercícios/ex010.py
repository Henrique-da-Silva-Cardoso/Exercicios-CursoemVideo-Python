din = float(input('\033[4;36mQuantos reais você tem na carteira? R$'))

print(f'Esse(s) \033[33mR${din:.2f}\033[m equivale(m) a \033[31mUSD{din/5.195:.2f}\033[m')

print(f'Esse(s) \033[33mR${din:.2f}\033[m equivale(m) a \033[35mEUR{din/6.345:.2f}\033[m')

print(f'Esse(s) \033[33mR${din:.2f}\033[m equivale(m) a\033[32m Yens {din*19.8965:.2f}\033[m')
