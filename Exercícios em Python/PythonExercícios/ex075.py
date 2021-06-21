valores = (int(input('Digite o primeiro valor: ')), int(input('Digite o segundo valor: ')),
           int(input('Digite o terceiro valor: ')), int(input('Digite o quarto valor: ')))

print(f'Você digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3)+1}ᵃ vez')
else:
    print('O valor 3 não foi inserido nenhuma vez')
print('Os números pares foram:', end=' ')
for c in valores:
    if c % 2 == 0:
        print(c, end=' ')
