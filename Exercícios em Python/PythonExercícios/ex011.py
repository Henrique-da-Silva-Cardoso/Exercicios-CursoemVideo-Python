alt = float(input('Qual a altura dessa parede? '))
lar = float(input('Qual a largura dessa parede? '))
area = alt*lar

print(f'A área da parede com \033[{alt}m de altura e {lar}m de largura é {area}m² e a litragem de tinta necessária para pintá-la é {area/2}l')
