print('-'*30)
print(f'{"MAIOR E MENOR":^30}')
print('-'*30)
val = []
for cont in range(0, 5):
    val.append(int(input(f'Digite um valor para a {cont}° posição: ')))
print('-'*30)
print(f'Você digitou os valores: {val}')
print(f'O maior valor digitado foi {max(val)} e sua posição é: ', end='')
for c, v in enumerate(val):
    if v == max(val):
        print(f'{c}', end='... ')
print(f'\nO menor valor digitado foi {min(val)} e sua posição é: ', end='')
for c, v in enumerate(val):
    if v == min(val):
        print(f'{c}', end='... ')
