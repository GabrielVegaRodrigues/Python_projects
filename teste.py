nome = input('digite o nome da cidade')
min = nome.lower()
dividido = min.split()
cont = dividido[0].count('santo')
if cont == 1:
    print('tem santos')
else:
    print('nao tem santos')