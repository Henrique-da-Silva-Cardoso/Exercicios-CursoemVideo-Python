metros = float(input('Digite quantos metros você quer medir: '))

print(f'A medida de \033[4m{metros}\033[m equivale a :')
print(f'\033[4m{metros/1000}\033[mkm')
print(f'\033[4m{metros/100}\033[mhm')
print(f'\033[4m{metros/10}\033[mdam')
print(f'\033[4m{metros*10}\033[mdm')
print(f'\033[4m{metros*100}\033[mcm')
print(f'\033[4m{metros*1000}\033[mmm')
