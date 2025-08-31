# Escribe un programa que genere un número secreto aleatorio entre 1 y 100. El usuario debe intentar adivinar
# este número. Después de cada intento, el programa debe darle una pista al usuario, indicando si el número que
# ingresó es mayor o menor que el número secreto. El juego termina cuando el usuario adivina el número.

import random as rand # libreria para generar un numero aleatorio



numeroSecreto = rand.randint(1, 100)
# print(numeroSecreto)
while True:
    try:
        numero = int(input("Adivina el número: "))
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número.")
        continue

    if numero == numeroSecreto:
        print("El numero es correcto")
        break
    elif numero < numeroSecreto:
        print("El numero es mayor")
    elif numero > numeroSecreto:
        print("El numero es menor")