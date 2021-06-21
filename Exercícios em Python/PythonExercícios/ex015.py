dia = int(input('Quantos dias o carro foi alugado por? '))
dist = float(input('Quantos quilômetros fora rodados? '))
t = dia*60 + dist*0.15

print(f'O total a pagar é R$\033[32m{t:.2f}\033[m')
