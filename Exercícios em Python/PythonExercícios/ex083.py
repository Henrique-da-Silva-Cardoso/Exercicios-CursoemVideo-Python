# Versão do professor Guanabara, consiste em adicionar e retirar elementos de uma lista
# Resolvi deletar minha versão que anteriormente achei estar correta por causa de bugs, para consertá-los
# teria de se aumentar a complexidade do código, tornando inútil o intuito original de um código simples
expr = str(input('Digite uma expressão matemática: ')).strip()
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')