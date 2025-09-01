'''
Metodo 'strip()'
Se utiliza para eliminar caracteres especificados al inicio y al final de una cadena de caracteres. Si no se especifica
se eliminaran espacios en blanco y saltos de linea
'''

cadena = 'Hello World'
print(cadena.strip('dH'))

'''
Metodo 'rstrip()'
Se utiliza para eliminar únicamente caracteres especificados al final de una cadena. Si no se especifica uno o mas
caracteres a eliminar, solo eliminara espacios en blanco y saltos de linea
'''

cadena2 = "Hello World"
print(cadena2.rstrip('dH'))

'''
Metodo 'lstrip()'
Se utiliza para eliminar únicamente caracteres especificados al inicio de una cadena. Si no se especifica uno o mas
caracteres a eliminar, solo eliminara espacios en blanco y saltos en linea
'''

cadena3 = "Hello World"
print(cadena3.lstrip('dH'))