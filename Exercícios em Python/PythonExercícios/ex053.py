'''frase = str(input('Digite uma frase qualquer: ')).replace(' ', '').upper()
for c in range(0, len(frase)):
    if frase[c] != frase[-c-1]:
        print('Não é um palíndromo')
        exit()
print('É um palíndromo')'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if junto == inverso:
    print('Por isso é um palíndromo')
else:
    print('Por isso não é um palíndromo')
