# La compañoa multinacional Rappi, solicita un sistema que determine los ias de vacaciones a los que tiene derecho un
# trabajaor, tomando en cuenta las siguientes caracteristicas:
# Existen tres departamentos dentro de la compañia con sus respectivas claves:
# 1. Departamento de Atension al cliente (clave 1)
# 2. Departamento de Logistica (clave 2)
# 3. Gerencia. (clave 3)
# Trabajadores con clave 1, 2, 3 (Atencion al cliente, Logistica, Gerencia)
# Con 1 año de servicio, reciben 6, 7, 10 dias de vacaciones
# Con 2 a 6 años de servicio reciben 14, 15, 20 dias de vacaciones
# A partir de 7 años de servicio, reciben 20, 22, 30 dias de vacaciones
# El sistema debe de solicitar el nombre, clave del departamento y atiguedad del trabajador desde teclado
# Posteriormente el programa debe mostrar un mensaje en pantalla, que contenga el nombre del trabajador y los
# dias de vacaciones a los que tiene derecho

print("Bienvenido al sistema de informacion de tus dias de vacaciones")


while True:
    nombre = input("Nombre: ")
    claveDep = int(input("Clave:"
                         "\n1. Departamento de Atencion al Cliente"
                         "\n2. Departamento de Logistica"
                         "\n3. Gerencia\n"))
    # if claveDep > 3 or claveDep < 1:
    #     print("Elige una de las 3 opciones")
    #     continue
    while claveDep != 1 and claveDep != 2 and claveDep != 3:
        print("Opcion invalida")
        claveDep = int(input("Clave:"
                             "\n1. Departamento de Atencion al Cliente"
                             "\n2. Departamento de Logistica"
                             "\n3. Gerencia\n"))
    antiguedad = int(input("Antiguedad: "))

    if claveDep == 1:
        if antiguedad == 1:
            print(nombre,"recibes 6 dias de vacaciones")
        elif antiguedad > 1 and antiguedad < 7:
            print(nombre,"recibes 14 dias de vacaciones")
        elif antiguedad > 7:
            print(nombre,"recibes 20 dias de vacaciones")
    elif claveDep == 2:
        if antiguedad == 1:
            print(nombre, "recibes 7 dias de vacaciones")
        elif antiguedad > 1 and antiguedad < 7:
            print(nombre, "recibes 15 dias de vacaciones")
        elif antiguedad > 7:
            print(nombre, "recibes 25 dias de vacaciones")
    elif claveDep == 3:
        if antiguedad == 1:
            print(nombre, "recibes 10 dias de vacaciones")
        elif antiguedad > 1 and antiguedad < 7:
            print(nombre, "recibes 20 dias de vacaciones")
        elif antiguedad > 7:
            print(nombre, "recibes 30 dias de vacaciones")

    opc = int(input("¿Deseas realizar una nueva consulta?\n1. Si\n2. No\n"))
    while opc != 1 and opc != 2:
        print("Opcion invalida")
        opc = int(input("¿Deseas realizar una nueva consulta?\n1. Si\n2. No\n"))

    if opc == 2:
        print("Adios...")
        break