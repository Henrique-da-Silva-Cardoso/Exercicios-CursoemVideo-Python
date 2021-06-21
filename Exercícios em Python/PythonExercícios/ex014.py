temp = float(input('Informe a temperatura em °C: '))

print(f'A temperatura de \033[33m{temp}°C\033[m corresponde a \033[31m{(temp * 9/5)+32}°F\033[m e a \033[34m{temp+273.15}K\033[m')