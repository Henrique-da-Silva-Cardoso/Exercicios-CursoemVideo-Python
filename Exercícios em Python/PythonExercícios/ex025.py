nome = input('Escreva seu nome: ').strip()

print(f'Tem Silva no seu nome? ')

if "Silva" in nome.title():
    print('\033[32mTrue')
else:
    print('\033[31mFalse')