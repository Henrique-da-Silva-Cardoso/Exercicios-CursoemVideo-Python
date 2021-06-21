from random import randint

nome = input('Digite seu nome completo: ').strip()

print(f'Seu nome com as letras todas maiúsculas é \033[{randint(30, 37)}m{nome.upper()}\033[m')

print(f'Seu nome com as letras todas minúsculas é \033[{randint(30, 37)}m{nome.lower()}\033[m')

Div= nome.split()

print(f'Desconsiderando espaços seu nome possui \033[{randint(30, 37)}m{len(nome.replace(" ", ""))}\033[m letras')

print(f'Seu primeiro nome é {Div[0]} e possui \033[{randint(30, 37)}m{len(Div[0])}\033[m letras')
