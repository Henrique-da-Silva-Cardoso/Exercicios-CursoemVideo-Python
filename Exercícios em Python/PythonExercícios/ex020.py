from random import sample

n1 = input('Alune um: ')
n2 = input('Alune dois: ')
n3 = input('Alune três: ')
n4 = input('Alune quatro: ')

ns = [n1, n2, n3, n4]

print(f'A sequência de quem irá apagar o quadro nos próximos dias será \033[35m{sample(ns, k=4)}')
