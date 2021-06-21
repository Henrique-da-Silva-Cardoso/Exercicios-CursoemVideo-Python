while True:
    numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
               'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

    index = int(input('Digite um valor entre 1 e 20: '))
    while index < 0 or index > 20:
        index = int(input('Inválido. Digite um valor entre 0 e 20: '))

    print(f'Você digitou o número {numeros[index]}')
    esc = str(input('Você quer continuar? [S/N]: ')).strip()[0]
    if esc in 'Nn':
        break
print('Fechando o programa, volte sempre!')
