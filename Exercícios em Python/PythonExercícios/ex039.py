from datetime import date
data = date.today().year
ano_nasc = int(input('Qual o seu ano de nascimento? '))
gen = str(input('Qual seu gênero, digite h para se designar homem, m para se designar mulher e n para'
          ' se designar não-binárie '))
idade = data - ano_nasc

if gen == 'h':
    if idade < 18:
        print(f'Você ainda vai se alistar no exército! Falta(m) {18 - idade} ano(s) para isso acontecer')
    elif idade == 18:
        print('Está na hora de se alistar! Vá lá soldado!')
    else:
        print(f'Já passou da hora de você se alistar! Você está {idade - 18} ano(s) atrasado!')
        print(f'Você deveria ter se alistado no ano {data - (idade - 18)}')
elif gen == 'm':
    print('\033[30;46mO alistamento militar não é obrigatório para pessoas com gênero'
          ' diferente do masculino, porém é sua opção se alistar.\033[m')
    if idade < 18:
        print(f'Você ainda vai se alistar no exército! Falta(m) {18 - idade} ano(s) para isso acontecer')
    elif idade == 18:
        print('Está na hora de se alistar! Vá lá soldada!')
    else:
        print(f'Já passou da hora de você se alistar! Você está {idade - 18} ano(s) atrasada!')
        print(f'Você deveria ter se alistada no ano {data - (idade - 18)}')
elif gen == 'n':
    print('\033[30;46mO alistamento militar não é obrigatório para pessoas com gênero'
          ' diferente do masculino, porém é sua opção se alistar.\033[m')
    if idade < 18:
        print(f'Você ainda vai se alistar no exército! Falta(m) {18 - idade} ano(s) para isso acontecer')
    elif idade == 18:
        print('Está na hora de se alistar! Vá lá soldade!')
    else:
        print(f'Já passou da hora de você se alistar! Você está {idade - 18} ano(s) atrasade!')
        print(f'Você deveria ter se alistade no ano {data - (idade - 18)}')
else:
    print('Por favor insira um valor válido para o gênero quando reiniciar o programa')
