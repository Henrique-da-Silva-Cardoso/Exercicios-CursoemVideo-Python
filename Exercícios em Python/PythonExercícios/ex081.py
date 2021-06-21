nums = []
while True:
    nums.append(int(input('Digite um valor: ')))
    esc = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    while esc not in 'SsNn':
        esc = str(input('Comando inválido digite novamente [S/N]: ')).strip()[0]
    if esc in 'Nn':
        break
print('-='*30)
print(f'Foram digitados {len(nums)} números')
nums.sort(reverse=True)
print(f'Os números digitados em forma decrescente foram {nums}')
if 5 in nums:
    print('O número 5 está presente na lista')
else:
    print('O número 5 não está presente na lista')
