# ----------------------- ACCEDER A LOS ELEMENTOS DE UNA CADENA -----------------------

print("Para acceder a un elemento usamos: "[1])
print("Para imprimir el ultimo elemento de mi cadena se coloca [-1]"[-1])
print("Para imprimir de inicio a una posicion usamos: "[:4])
print("Para acceder a un substring a partir de una posicion usamos: "[5:12])
print("Para acceder al resto de caracteres a partir de una posicion usamos: "[5:])

# ----------------------- OPERACIONES Y MÉTODOS COMUNES CON CADENAS -----------------------

nombre = "Jovani"
apellido = "Hernandez"

concatenacion = nombre + " " + apellido
print("\n\nConcatenacion:",concatenacion)
print("Longitud de cadena:", len(concatenacion))
print("Nombre en mayusculas:",nombre.upper())
print("Apellido en minusculas:",apellido.lower())
print("Busqueda de cadena:", concatenacion.find("Hernandez"), "Nos devuelve la posicion donde se encontro" )
print("Remplazar subcadena:", concatenacion.replace("Hernandez","Sanchez"))

# ----------------------- FORMATEO DE CADENAS DE TEXTO Y F-STRINGS -----------------------
nombre = "Yonathan"
edad = 18
cadena = f"\n\nMi nombre es {nombre} y tengo {edad}"
print(cadena)

