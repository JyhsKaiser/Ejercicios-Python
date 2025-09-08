'''
Desarrollar un programa que elimine una palabra que forme parte de una cadena de caracteres.
    La cadena de caracteres degbera ser solicitada desde teclado.
    La palabra a eliminar debera ser solicitada desde el teclado.
'''

cadena = 'hola mundo bebe'
palabra = 'mundo'
# cadena = input('Escribe tu cadena de caracteres:')
# palabra = input('Escribe tu palabra a eliminar:')

subcadena = cadena.replace(palabra+' ','')
print(subcadena)

posicion_inicial = cadena.find(palabra)
posicion_final = posicion_inicial + len(palabra) + 1
cad1 = cadena[0:posicion_inicial]
cad2 = cadena[posicion_final:]
cadena = cad1 + cad2
print(cadena)

cadena = 'hola mundo bebe'
pos_ini = cadena.find(palabra)
sub_string = cadena[0  : pos_ini] + cadena[pos_ini + len(palabra) + 1:]
print(sub_string)