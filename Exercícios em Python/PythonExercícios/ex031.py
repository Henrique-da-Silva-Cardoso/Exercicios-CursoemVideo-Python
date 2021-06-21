dist = int(input('Digite a distância da viagem de ônibus: '))
preço = dist * 0.5 if dist <= 200 else dist * 0.45
print(f'O preço a ser pago por uma viagem de {dist}km é \033[32mR${preço}')
