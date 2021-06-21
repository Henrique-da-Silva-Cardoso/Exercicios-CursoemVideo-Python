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

c = 0
while c < 10:
    print(f'{num}', end=' → ')
    num += r
    c += 1
print('Acabou')
