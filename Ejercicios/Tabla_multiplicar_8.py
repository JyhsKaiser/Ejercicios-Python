
print('tabla de multiplicaciones'.title().center(50,'_'))
numero = int(input('Ingresa un numero: '))
for i in range(1, 11):
    print(f'{numero} x {i} = {numero * i}')