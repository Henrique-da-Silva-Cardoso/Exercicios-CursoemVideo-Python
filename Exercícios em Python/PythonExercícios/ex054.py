from datetime import date
mr = 0
mn = 0
for c in range(0, 7):
    ano = int(input('Digite seu ano de nascimento: '))
    ano = date.today().year - ano
    if ano >= 21:
        mr += 1
    elif ano < 21:
        mn += 1
print(f'{mr} pessoas são de maior e {mn} pessoas não são')
