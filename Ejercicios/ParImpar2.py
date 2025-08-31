# Desarrollar un programa que solicite un numero entero desde teclado al usuario, posteriormente el programa
# debera determinar e indicar a traves de un mensaje, si el numero introducido es par o impar
# El mensaje en pantalla debera mostrar la frase el numero es par o impar, junto con el numero que el usuario introdujo
# desde teclado

numero = int(input("dame un numero"))
if numero % 2 == 0:
    print(numero, "es par")
else:
    print("El numero",numero, "es impar")