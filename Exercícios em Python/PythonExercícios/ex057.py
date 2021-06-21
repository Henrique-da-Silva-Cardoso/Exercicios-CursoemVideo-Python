sex = str(input('Digite o seu sexo: [M/F] ')).strip().upper()[0]

while sex != 'M' and sex != 'F':
    sex = str(input('Sexo digitado anteriormente é inválido, digite novamente ')).upper().strip()[0]

if sex == 'M':
    print('Obrigado pela cooperação senhor')
elif sex == 'F':
    print('Obrigado pela cooperação senhora')
