vcasa = float(input('Qual o valor da casa a ser comprada? R$'))
sal = float(input('Qual o seu salário? R$'))
tem = (int(input('Em quantos anos você pretende pagar essa casa? ')))
par = vcasa/(tem*12)
print(f'Uma casa de R${vcasa:.2f} sendo paga em {tem} anos terá uma prestação de {prest:.2f}')
if prest > 0.3*sal:
    print('\033[4;31mEmpréstimo negado, parcela excede 30% do salário')
else:
    print('\033[4;32mEmpréstimo aprovado! Bem vindo a sua nova casa!')
