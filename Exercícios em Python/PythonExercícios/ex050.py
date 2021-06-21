s = 0
for c in range(1, 7):
    n = int(input(f'Insira o {c}° número: '))
    if n % 2 == 0:
        s += n
print(f'A soma de todos os números pares inseridos vale {s}')