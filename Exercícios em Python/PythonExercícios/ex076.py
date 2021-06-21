print('\033[34m-'*46)
print(f'{"LISTAGEM DE PREÇOS":^46}')
print('-'*46+'\033[m')
prod = ('Leite Condensado', 3.99,
        'Máscara Descartável', 27.98,
        'Cabeçote de Motor', 1241.03,
        'Livro Pequeno Príncipe', 60.00,
        'RTX8000', 80655.00,
        'Teclado RGB Gamer', 290.00,
        'Espanador', 24.99,
        'Sapatenis Supreme', 0.02,
        'Vestido de Morango',75.00,
        'Blu-Ray Coringa', 25.00,
        'Cosplay Bakugo Completo', 560.00)
for c in range(0, len(prod), 2):
    print(f'{prod[c]:.<35}R${f"{prod[c+1]:.2f}":>9}')
print('\033[34m', end='')
print('-'*46)