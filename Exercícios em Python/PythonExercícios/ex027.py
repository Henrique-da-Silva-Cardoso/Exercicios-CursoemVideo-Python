nome = input('Digite seu nome: ').strip()

div = nome.split()

print(f'Seu primeiro nome é \033[32m{div[0]}\033[m')
div.reverse()
print(f'Seu último nome é \033[31m{div[0]}\033[m')

# print(f`Seu último nome é {div[len(nome)-1]}
