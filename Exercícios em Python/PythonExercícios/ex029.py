carro = int(input('Digite a velocidade do carro: '))

if carro > 80:
    print(f'\033[4;30;41mVocê foi multado por alta velocidade e tem de pagar R${(carro-80)*7}\033[m')
else:
    print('Obrigado por obedecer as leis de trânsito!')
