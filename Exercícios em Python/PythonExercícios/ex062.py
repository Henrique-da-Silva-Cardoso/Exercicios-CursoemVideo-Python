print('='*40)
print('    OS 10 PRIMEIROS TERMOS DE UMA PA')
print('='*40)

num = int(input('Digite o primeiro termo da progressão aritmética: '))
r = int(input('Digite a razão aritmética: '))

if r == 0:
    print('Essa progressão aritmética é constante ')
elif r > 0:
    print('Essa progressão aritmética é crescente ')
elif r < 0:
    print('Essa progressão aritmética é decrescente ')

cont = 0
m = 0
while cont < 10 + m:
    print(f'{num}', end=' → ')
    num += r
    cont += 1
    if cont == 10 + m:
        print('PAUSA')
        m = int(input('\nQuantos mais termos você quer mostrar? ')) + m

print(f'A progressão acabou e mostrou {cont} números')
