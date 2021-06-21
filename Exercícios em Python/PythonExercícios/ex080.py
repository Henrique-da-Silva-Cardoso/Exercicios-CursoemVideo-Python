val = []
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > val[-1]:
        print('Adicionado no final da lista.')
        val.append(num)
    else:
        for b in range(0, len(val)):
            if num < val[b]:
                print(f'Adicionao na posição {b}.')
                val.insert(b, num)
                break
print('-='*15)
print(f'Os valores digitados foram {val}')
