'''
Clase range:
Genera secuencias de numeros inmutables, es deci, que no se pueden modificar, estas secuencias se generan a partir de
un rango previamente establecido. Generalmente se usa como objeto iterable dentro de la sintaxis del ciclo o bucle
for. Esta nos permite trabajar con un minimo de un argumento y un máximo de 3 argumentos de manera simultanea

range ( start, stop, step )

:argument
    start: int, indica el numero a partir del cual se comenzara a generar la secuencia de numeros
    stop: valor entero que indica el numero hasta el cual se va a generar la secuencia de numeros
    step: int, indica el incremento o decremento de la sucesion numerica entre un numero y el siguiente

'''
for i in range(1, 11):
    print(i,i, end=' ', sep=',')