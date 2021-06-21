from datetime import date
nasc = int(input('Insira seu ano  de nascimento: '))
ano = date.today().year
idade = ano - nasc

print(f'Sua idade é {idade} anos')

if idade <= 9:
    print('\033[35mMIRIM')
elif idade <= 14:
    print('\033[35mINFANTIL')
elif idade <= 19:
    print('\033[36mJUNIOR')
elif idade <= 25:
    print('\033[36mSÊNIOR')
elif idade > 25:
    print('\033[33mMASTER')
