censo = []
pessoa = {}
cont, media = 0, 0

while True:
    pessoa['nome'] = input('Digite seu nome: ')
    pessoa['sexo'] = input('Digite seu sexo [M/F/O]: ')
    while pessoa['sexo'] not in 'MmFfOo':
        pessoa['sexo'] = input('Sexo Inválido! Digite novamente: [M/F/O] ')
    pessoa['idade'] = int(input('Digite sua idade: '))

    censo.append(pessoa.copy())
    cont += 1
    esc = input('Quer continuar? [S/N]: ')
    while esc not in 'SsNn':
        print('ERRO! Responda apenas S ou N.')
        esc = input('Quer continuar? [S/N]: ')
    if esc in 'Nn':
        break

for c in censo:
    media += c['idade']
media /= cont
print('-='*40)
print(f'A) Foram cadastradas {cont} pessoas')
print(f'B) A média da idade do grupo é {media} anos')
print('C) As mulheres cadastradas foram: ', end='')
for c in censo:
    if c['sexo'] in 'Ff':
        print(c['nome'], end=' ')
print('\nLista das pessoas que estão acima da média de idade: \n')
for c in censo:
    if c['idade'] > media:
        print(f'nome = {c["nome"]}; sexo = {c["sexo"]}; idade = {c["idade"]}')
print('-=' * 40)
print(f'{"<<<ENCERRADO>>>":^80}')
