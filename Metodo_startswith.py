'''
Metodo startswith():
Comprueba si una cadena de caracteres comienza con una subcadena en particular.
Ademas es posible establecer un rango de busqueda dentro de la cadena principal.

argumentos:
    subcadena: Se manda la subcadena para comprobar
    posicion_inicio: Se manda desde donde se analizara la cadena principal
    posicion_final: Se mande hasta donde se analizara la cadena principal

:return:
    Nos devuelve un valor booleano, si empieza con la subcadena devuelve True, si no, False

'''
print('Esta cadena sera usada'.startswith('a',0, 10))       # False

# En caso de que no se especifique un inicio o un final se tomara en cuenta toda la cadena
print('Esta cadena sera usada'.startswith('Esta'))      # True


