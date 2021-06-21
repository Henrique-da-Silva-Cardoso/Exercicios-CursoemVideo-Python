pre = float(input('Qual o preço do produto? R$'))

print(f'R$\033[31m{pre}\033[m é o preço antigo do produto, R$\033[36m{pre-pre*0.05:.2f}\033[m é o novo preço')
