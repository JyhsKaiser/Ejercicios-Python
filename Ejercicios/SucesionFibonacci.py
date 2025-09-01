'''
Desarrollar un programa que imprima en pantalla la sucesion de fibonacci desde el numero 0 hasta el 1597 de manera
horizontal
'''
x, y, z= 0, 1, 0
print(x,y,end=' ')
while z != 1597:
    z = x + y
    x, y = y, z
    print(z,end=' ')
