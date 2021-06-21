frase = str(input('Digite uma frase qualquer: ')).upper().strip()

print(f'O número de vezes que a letra A aparece na frase é \033[30m{frase.count("A")}\033[m')

print(f'O primeiro A aparece como o caractere \033[35m{frase.find("A")+1}\033[m')

print(f'O último A aparece como o caracter \033[35m{frase.rfind("A")+1}\033[m')
