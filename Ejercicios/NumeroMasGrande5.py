'''
Desarrollar un programa que solicite tres números enteros desde el teclado al usuario, posteriormente, el programa
debera determinar e indicar a através de un mensaje en pantalla, cual de los 3 números es el más grande

El mensaje en pantalla deberá mostrar el número que resulto ser el más grande de los 3
'''
numeros = []
for indice in range(0,3):
    numeros.append(int(input(f'Dame el numero {indice+1}: ')))

numeros.sort()
print(f'De la siguiente lista de numeros {numeros} el numero mas grande es:',numeros[-1])