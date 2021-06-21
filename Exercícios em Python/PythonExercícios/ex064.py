num = cont = soma = 0
while num != 999:
    num = int(input('Digite um número aleatório [999 para sair]: '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'A soma de todos os {cont} números inseridos é {soma}')
