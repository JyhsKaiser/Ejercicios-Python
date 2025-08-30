verdadero = True
falso = False

print("Podemos utilizar operadores logicos tanto como 'and' o '&' ejemplo:", verdadero and falso,"o", verdadero & falso)

# ----------------------- CONVERSION DE TIPOS A BOOLEANOS Y EVALUACIUN DE EXPRESIONES -----------------------
numero = 43     # Si mi numero es cero me dara un false pero si es diferente de cero me dara true
cadena = "Hola"
cadenaVacia = ""        #Si mi cadena esta vacia me retornara un false la funcion bool
boolNumero = bool(numero)
boolCadena = bool(cadena)
boolCadenaVacia = bool(cadenaVacia)
print(boolNumero, boolCadena, boolCadenaVacia)