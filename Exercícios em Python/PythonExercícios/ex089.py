from time import sleep
boletim = []
while True:
    nome = str(input('Nome: ')).strip()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    boletim.append([nome, [nota1, nota2], media])
    esc = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    if esc in 'Nn':
        break
print('''=-=-=-=-=-==-=-=-=-=-=-=-=-==-=-=-=-=-==-=-=-=-=-=-=-=-==-=-=-=-=-==-=-=-=-=-=-=-=-=
No. NOME               MÉDIA 
------------------------------''')
for posicao, aluno in enumerate(boletim):
    print(f'{posicao:<3} {aluno[0]:<20} {aluno[2]:.1f}')
print('-'*30)
while True:
    esc = int(input('Mostrar as notas de qual aluno? (Negativo interrompe): '))
    while esc > len(boletim)-1:
        esc = int(input('Número inválido, tente novamente. (Negativo interrompe): '))
    if esc < 0:
        break
    else:
        print(f'As notas de {boletim[esc][0]} são {boletim[esc][1]} ')
    print('-' * 30)
print('Finalizando...')
sleep(1)
print('Volte sempre!')
print('='*30)
