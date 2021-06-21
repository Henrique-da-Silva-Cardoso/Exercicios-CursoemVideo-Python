from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

print(f'Com o cateto oposto sendo \033[31m{co}cm\033[m e o cateto adjacente sendo \033[34m{ca}cm\033[m sua hipotenusa será \033[35m{hypot(co, ca):.2f}cm\033[m')