total, c, c_alto = 0, 0, 0  # c significa contador neste caso
precobaixo, nomebaixo = None, None
print(f'\033[32m{"CHECAGEM DE PRODUTOS":=<30}\033[m')
while True:
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$'))
    while preco < 0.01 and not preco == 0:
        # O valor monetário não pode ser menor do que um centavo, mas pode ser de graça
        preco = float(input('Valor inválido, preço muito baixo. Digite novamente: R$'))

    print('\033[35m-='*15+'-\033[m')
    total += preco
    if preco > 1000:
        c_alto += 1

    if c == 0 or preco < precobaixo:
        precobaixo = preco
        nomebaixo = nome
        c += 1
    esc = str(input('Deseja sair do programa? [S/N] ')).strip()[0]
    if esc in 'Ss':
        break

print(f'''{"MENU FINAL, OBRIGADO POR UTILIZAR O PROGRAMA E VOLTE SEMPRE":=^77}
┌───────────────────────────────────────────────────────────────────────────┐
│{f"O total gasto na compra desses {c} produtos foi R${total:.2f}":^75}│
│{f"A quantidade de produtos inseridos acima de R$1000 foi de {c_alto}":^75}│
│{f"O nome do produto mais barato é {nomebaixo} custando R${precobaixo:.2f}":^75}│
└───────────────────────────────────────────────────────────────────────────┘
''')
