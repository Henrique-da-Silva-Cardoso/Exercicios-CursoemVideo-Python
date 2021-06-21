alune = dict()
alune['Nome'] = str(input('Digite o nome de alune: ')).strip()
alune['Média'] = float(input(f'Digite a média de {alune["Nome"]}: '))

if alune['Média'] >= 7:
    alune['Situação'] = 'Aprovado'
elif alune['Média'] >= 6:
    alune['Situação'] = 'Recuperação'
else:
    alune['Situação'] = 'Reprovado'

for k, v in alune.items():
    print(f'{k} é igual a {v}')


