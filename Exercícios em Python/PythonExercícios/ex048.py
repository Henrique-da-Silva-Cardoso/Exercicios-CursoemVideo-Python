s = 0
cont = 0
for c in range(0, 501, 3):
    if c % 2 != 0:
        s += c
        cont += 1
print(f'A somatória de todos os {cont} múltiplos de três de 1 a 500 é {s}')
