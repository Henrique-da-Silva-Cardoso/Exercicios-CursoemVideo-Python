from time import sleep
r1 = float(input('Digite o comprimento do primeiro segmento de reta: '))
r2 = float(input('Digite o comprimento do segundo segmento de reta: '))
r3 = float(input('Digite o comprimento do terceiro segmento de reta: '))
print('\033[33m▼\033[m'*25)
print('Analisando triângulo...')
print('\033[33m▲\033[m'*25)
sleep(3)

if r3 < r1 + r2 and r2 < r1 + r3 and r1 < r2 + r3:
    print('\033[32mConfigura um triângulo!')
else:
    print('\033[31mNão Configura um triângulo!')
