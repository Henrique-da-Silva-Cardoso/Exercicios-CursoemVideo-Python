num = int(input('Digite quantos números da sequência de Fibonacci você quer ver: '))
n1, n2 = 0, 1
c = 0
while num <= 0:
    num = int(input('Digite um número acima de zero por favor '))
print('~'*100)
while c < num:
    print(n1, end=' → ')
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    c += 1
    if c == num:
        print('Cabô')
print('~'*100)

