num = int(input('Digite um número: '))

print(f'O dobro do número \033[31m{num}\033[m é \033[33m{num*2}\033[m\nSeu triplo é \033[36m{num*3}\033[m\nSua raiz quadrada é \033[46m{pow(num, 0.5):.2f}\033[m')

