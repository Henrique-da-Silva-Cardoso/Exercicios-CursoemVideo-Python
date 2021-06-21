valor = float(input('Digite o valor do produto: '))
pagar = str(input('Digite a forma de pagamento dentre as disponíveis'
                  '\n          dinheiro, cheque ou cartão'
                  '\n  dinheiro e cheque possuem 10% de desconto'
                  '\n                       ')).strip()

if pagar == 'dinheiro' or pagar == 'cheque':
    print(f'O valor total à se pagar é \033[33mR${valor - valor * 0.1}')
elif pagar == 'cartão':
    vezes = int(input('Em quantas vezes irá querer pagar no cartão?\n'
                      '1x ou à vista com 5% de desconto, 2x com o preço normal ou 3x ou mais com 20% de juros? '))
    if vezes == 1:
        print(f'O valor total à se pagar é \033[33mR${valor - valor*0.05}')
    elif vezes == 2:
        print(f'O valor total à se pagar é \033[33mR${valor}\033[m com 2 parcelas de \033[35m{valor/2}')
    else:
        print(f'O valor total à se pagar é \033[33mR${valor + valor*0.2}\033[m com {vezes} parcelas de \033[31mR${(valor + valor*0.2)/vezes}')
else:
    print('Nenhum método válido de pagamento foi selecionado por favor reinicie o programa.')
