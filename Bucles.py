# ----------------------- BUCLE FOR -----------------------

# Listas
nombres = ["Jovani", "Pepe", "Joaquin", 4, 1 + 3j]
for nombre in nombres:  # Nos iterara en cada posicion de nuestra lista nombres
    print(nombre, " \n")

for i in range(3):  # la funcion range() nos permitira iterar el numero de veces que se coloque dentro
    print(i + 1)
print("\n")
for i in range(2, 7):  # De este modo empieza en la posicion 2 e itera hasta la posicion 7
    print(i)
print("\n")
for i in range(1, 10, 2): # De este modo empieza en 1 hasta 7 llendo de 2 en 2
    print(i)
print("\n")
for i in range(10, -1, -1): # para hacer que vaya al revez
    print(i)
print("\n")
frase = "Hola!!"
for letra in frase:     # De esta forma podemos iterar una cadena
    print(letra)
print("\n")
numeros, suma = [1, 2, 3, 4, 5], 0  # Declaramos un array
for numero in numeros:
    suma += numero
print(suma)
print("\n")
matriz = [      # Declaramos una matriz
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for fila in matriz:     # Aqui utilizaremos los for anidados
    for columna in fila:
        print(columna, end=" ")     #Usaremos la palabra reservada "end" sirve para configurar la forma en que acaba cada impresion
    print() # Nos hace el salto de linea

# ----------------------- BUCLE WHILE -----------------------
contador = 0
while contador < 5:
    print(contador)
    contador += 1

while True:
    if input("Escribe 'salir' para salir: ") == "salir":
        break