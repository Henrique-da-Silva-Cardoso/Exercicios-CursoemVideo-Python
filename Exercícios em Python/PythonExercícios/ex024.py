from time import sleep

cid = input('Escreva o nome de sua cidade: ').strip()
div = cid.split()

print(f'Será revelado se sua cidade começa com santo: ')
sleep(3)
if "Santo" in div[0].title():
    print('\033[32mTrue')
else:
    print('\033[31mFalse')
