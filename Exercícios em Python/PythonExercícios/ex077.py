palavras = ('Força', 'Orifício', 'Onibûs', 'Nervo', 'Carro', 'Bicicleta', 'Mão', 'Marcial')
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos:', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiouáéíóúàèìòùâêîôûãõ':
            print(letra.lower(), end=' ')
