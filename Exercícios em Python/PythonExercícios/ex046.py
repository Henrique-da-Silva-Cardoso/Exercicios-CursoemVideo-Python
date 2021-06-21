from time import sleep
from emoji import emojize
from datetime import date

for c in range (10, -1, -1):
    print(c)
    sleep(1)
print(emojize('\033[32m:fireworks:\033[m'*7))
print('Feliz', str(date.today().year) + '!')
print(emojize('\033[33m:fireworks:'*7))
