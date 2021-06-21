num = int(input('Digite um número inteiro: '))

if num > 1:
    for c in range(2, num+1):
        if num / c >= c:
            if num % c == 0:
                print('O número não é primo')
                print(f'{c} vezes {num//c} é {num}')
                break
        elif num / c < c:
            print('O número é primo')
            break
elif num == 1:
    print('O número 1 tem somente um número divisível que é ele mesmo, então não é primo')
else:
    print('Zero ou números negativos não são primos')
