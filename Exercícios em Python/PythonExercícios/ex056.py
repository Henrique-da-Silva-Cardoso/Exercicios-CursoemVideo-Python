fem_nova = 0
it = 0
maioridade = 0
nomem = ''

for c in range(1, 5):
    print(f'=========== {c}ª PESSOA ============')
    nome = str(input('Digite seu nome: ')).strip()
    sexo = str(input('Sexo [M/F/O]: ')).strip()
    idade = int(input('Digite sua idade: '))
    it += idade

    if c == 0 and sexo in 'Mm':
        maioridade = idade
        nomem = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomem = nome
    if sexo in 'Ff' and idade < 21:
        fem_nova += 1
mi = it / 4

print(f'A média de idade do grupo é {mi}')

if maioridade == 0:
    print('Não houve nenhum homem no grupo')
else:
    print(f'O nome do homem mais velho é {nomem}')

print(f'A quantidade de mulheres com idade menor de 21 anos é {fem_nova}')
