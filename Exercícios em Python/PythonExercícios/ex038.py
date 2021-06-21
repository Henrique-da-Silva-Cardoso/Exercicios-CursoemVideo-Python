n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('\033[4;36mO primeiro valor é maior')
elif n2 > n1:
    print('\033[4;33mO segundo valor é maior')
else:
    print('\033[1;3;4;35mNão existe valor maior. Os dois são iguais.')
