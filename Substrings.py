'''

cadena[ inicio : final : saltos]


Nota:
Los indices positivos se situaran desde el inicio de la cadena, haciendo su recorrido de izquierda a derecha.
Los indices negativos se situaran desde el final de la cadena, haciendo su recorrido de izquierda a derecha.
'''

cadena = '0123456789'
substring = cadena[ 0 : 5]
substring_negativo = cadena[  : -1]
substring_saltos = cadena[-5 :  : 2]
print(substring, substring_negativo, substring_saltos)