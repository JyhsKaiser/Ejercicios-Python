# ----------------------- SINTAXIS BASICA -----------------------
def saludo(nombre):
    print(f"Hola {nombre}")

# saludo(input("Ingresa tu nombre: "))
def suma(a, b):
    return a + b

print(suma(5, 4))


def suma(a, b=2):   # Si no le enviamos el valor de b la funcion tomara el valor por default que es 2
    return a + b

print(suma(5))

# ----------------------- VARIABLES LOCALES Y GLOBALES -----------------------
print("Variables locales y globales")
x = 10
def fun():
    y = 5
    print(x, y)

fun()
# ----------------------- FUNCIONES COMO OBJETOS Y ASIGNACION A VARIABLES -----------------------
print("Funciones como objetos")
def saludar():
    print("Hola")
saludo = saludar    # Es posible asignar una funcion a una variable ya que las funciones son objetos de primera clase
saludo()
saludar()

# ----------------------- FUNCIONES ANIDADAS -----------------------
print("Funciones anidadas")
def externa():
    x = 10
    def interna():
        print(x)

    interna()

externa()

# ----------------------- FUNCIONES RECURSIVAS -----------------------
print("Funciones recursivas")
def factorial(n):

    if n==1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))

# ----------------------- DOCSTRINGS -----------------------
def suma(a, b):
    """
    Calcular la suma de dos numeros
    :param a: Primer numero
    :param b: Segundo numero
    :return: int: la suma de a y b
    """
    return a + b
print(suma(5, 4))
