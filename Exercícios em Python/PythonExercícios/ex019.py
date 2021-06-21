from random import choice

n1 = input('Qual o nome do primeiro aluno: ')
n2 = input('Qual o nome do segundo aluno: ')
n3 = input('Qual o nome do terceiro aluno: ')
n4 = input('Qual o nome do quarto aluno: ')

ns = [n1,n2,n3,n4]

print(f'E alune escolhide para apagar o quadro foi \033[33m{choice(ns)}')
