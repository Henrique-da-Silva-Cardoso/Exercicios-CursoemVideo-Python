peso = float(input('Digite seu peso: '))
alt = float(input('Digite sua altura: '))
IMC = peso/alt**2

if IMC < 18.5:
    print(f'\033[36mAbaixo do peso ideal, IMC: {IMC:.2f}')
elif 18.5 <= IMC < 25:
    print(f'\033[32mPeso ideal, IMC: {IMC:.2f}')
elif 25 <= IMC < 30:
    print(f'\033[33mSobrepeso, IMC: {IMC:.2f}')
elif 30 <= IMC < 40:
    print(f'\033[35mObesidade, IMC: {IMC:.2f}')
elif IMC >= 40:
    print(f'\033[31mObesidade Mórbida, IMC: {IMC:.2f}')
