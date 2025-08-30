# ----------------------- SINTAXIS BASICA DE LA DECLARACION "if" -----------------------
x = 2
y = 3
if x > y:
    print("x es mayor que y")
if x < y:
    print("x es menor que y")
if x == y:
    print("x es igual a y")

print("\tCombinar varias condiciones".upper())

if x <= y and y > x:
    print("x es mayor que y")

# ----------------------- SINTAXIS BASICA DE LA DECLARACION "else" -----------------------
edad = 1
if edad >= 25 and edad <= 35:
    print("edad es menor que 35 y mayor que 25")
else:
    print("edad es menor que 25")

# ----------------------- SINTAXIS BASICA DE LA DECLARACION "elif" -----------------------
puntos = 1
if puntos >= 40:
    print("A")
elif puntos >= 30:
    print("B")
elif puntos >= 20:
    print("C")
else:
    print("D")
# ----------------------- ANIDAMIENTO DE ESTRUCTURAS CONDICIONALES -----------------------
edad = 33
nacionalidad = "MX"
if edad >= 18:
    if nacionalidad == "MX":
        print("El nacionalidad es MX")
    else:
        print("Tiene otra nacionalidad")
else:
    print("No es mayor de edad")
