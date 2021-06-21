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

for c in range(1, 11):
    print(f'{num}', end =' → ')
    num += r

print('Acabou')