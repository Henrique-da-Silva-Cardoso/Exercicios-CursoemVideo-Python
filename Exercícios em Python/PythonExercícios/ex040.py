n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota:' ))
med = (n1+n2)/2

if med < 5.0:
    print('\033[31mREPROVADO')
elif med >= 5.0 and med<7.0:
    print('\033[3;33mRECUPERAÇÃO')
else:
    print('\033[1;4;32mAPROVADO')
