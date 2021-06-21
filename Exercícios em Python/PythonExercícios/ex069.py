# c se refere a contador
cmaior, chomem, cmulher = 0, 0, 0
print('-'*26)
print(f'{"CADASTRE UMA PESSOA":^26}')
print('-'*26)
while True:
    print('\033[35m-='*13 + '-\033[m')
    sexo = str(input('Digite seu sexo [M/F/O]: ')).strip()
    idade = int(input('Digite sua idade: '))
    while sexo not in 'MmFfOo':
        sexo = str(input('Sexo digitado inválido, digite novamente [M/F/O]: ')).strip()[0]
    while idade < 0:
        idade = int(input('Informe sua idade real! Digite novamente: '))
    print('\033[35m-=' * 13 + '-\033[m')
    if idade >= 18:
        cmaior += 1

    if sexo in 'Mm':
        chomem += 1

    if idade < 20 and sexo in 'Ff':
        cmulher += 1
    esc = ' '
    while esc not in 'SsNn':
        esc = str(input('Quer parar de digitar? [S/N]: ')).strip()[0]
    if esc in 'Ss':
        break

print(f'\033[31mForam inseridas {cmaior} pessoas com mais de 18 anos\033[m')
print(f'\033[4;46mForam inseridos {chomem} homem(ns) \033[m')
print(f'\033[1;3;4;30;43mForam inseridas {cmulher} mulheres abaixo de 20 anos\033[m')
