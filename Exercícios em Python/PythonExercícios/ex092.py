from datetime import date
anoatual = date.today().year
info = {'nome': input("Digite seu nome: "),
        'idade': anoatual - int(input('Digite seu ano de nascimento: ')),
        'carteira': input('Digite sua carteira de trabalho, se não possuir uma digite 0: ')}

if info['carteira'] != '0':
    info['contratação'] = int(input('Digite o ano do seu contrato: '))
    info['salário'] = float(input('Digite o seu salário: R$'))
    info['aposentadoria'] = info['idade'] + 35 - (anoatual - info['contratação'])
    if info['aposentadoria'] - info['idade'] <= 0:
        info['aposent'] = 'Você já deveria ter se aposentado!'

print('-='*50)
for categ, val in info.items():
    print(f'- {categ} tem o valor {val}')
