from time import sleep
while True:
    n = int(input('\033[36mDigite o número o qual você quer a tabuada:\033[m '))
    if n < 0:
        break

    print('\033[36m-'*50)
    for c in range (1, 11):
        print(f' \033[35m{n}\033[m * \033[31m{c:2}\033[m = \033[33m{n * c}\033[m')
    print('\033[36m-'*50)
print('Desligando o programa TABUADA! Por favor, volte sempre!')
sleep(1)