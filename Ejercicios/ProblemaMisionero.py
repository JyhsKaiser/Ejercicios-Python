import random
import time


def busqueda_fuerza_bruta_aleatoria(canibales, misioneros):
    barca = []
    i, viajes = 0, 0

    orilla_izq = canibales + misioneros
    orilla_Der = []

    while True:
        try:
            if len(orilla_izq) == 2:
                num_rand1 = random.randint(0, len(orilla_izq) - 1)
                num_rand2 = random.randint(0, len(orilla_izq) - 1)
            else:
                num_rand1 = random.randint(0, len(orilla_izq) - 2 )
                num_rand2 = random.randint(0, len(orilla_izq) - 2)
        except ValueError:
            print("FIN")
            break

        if num_rand1 != num_rand2:
            barca.append(orilla_izq[num_rand1])
            barca.append(orilla_izq[num_rand2])
            print("--------------------------------------")
            if barca[0] in canibales and barca[1] in misioneros:
                orilla_Der,orilla_izq,barca,viajes = operaciones(orilla_Der, orilla_izq, barca, num_rand1, num_rand2, viajes)
            elif barca[0] in misioneros and barca[1] in canibales:
                orilla_Der,orilla_izq,barca,viajes = operaciones(orilla_Der, orilla_izq, barca, num_rand1, num_rand2, viajes)
            elif barca[0] in canibales and barca[1] in canibales:
                orilla_Der,orilla_izq,barca,viajes = operaciones(orilla_Der, orilla_izq, barca, num_rand1, num_rand2, viajes)

                num_canibales, num_misioneros = comprobar_cant_canibales_misioneros_izquierda(orilla_izq)
                if num_canibales > num_misioneros & num_misioneros != 0:
                    print('Los canibales se comieron a los misioneros, vuelve a intentarlo!!!!')
                    orilla_izq, orilla_Der, barca = restablecer(orilla_izq, orilla_Der, barca)
                    i += 1
                    print(f'EN LA ORILLA IZQUIERDA HAY:\ncanibales: {num_canibales} \nmisioneros: {num_misioneros}')
                    print("")
                    continue

            elif barca[0] in misioneros and barca[1] in misioneros:
                orilla_Der,orilla_izq,barca,viajes = operaciones(orilla_Der, orilla_izq, barca, num_rand1, num_rand2, viajes)
                num_canibales, num_misioneros = comprobar_cant_canibales_misioneros_izquierda(orilla_izq)

                if num_canibales > num_misioneros & num_misioneros != 0:
                    print('Los canibales se comieron a los misioneros, vuelve a intentarlo!!!')
                    orilla_izq, orilla_Der, barca = restablecer(orilla_izq, orilla_Der, barca)
                    i += 1
                    print(f'EN LA ORILLA IZQUIERDA HAY:\ncanibales: {num_canibales} \nmisioneros: {num_misioneros}')
                    continue


            num_canibales_der, num_misioneros_der = comprobar_cant_canibales_misioneros_derecha(orilla_Der)
            if num_canibales_der > num_misioneros_der & num_misioneros_der != 0:
                print('Los canibales se comieron a los misioneros, vuelve a intentarlo!!')
                orilla_izq, orilla_Der, barca = restablecer(orilla_izq, orilla_Der, barca)
                i += 1
                print(f'EN LA ORILLA DERECHA HAY:\ncanibales: {num_canibales_der} \nmisioneros: {num_misioneros_der}')
                continue

            if len(orilla_izq) == 0:
                i += 1
                break
    print("--------------------------------------")
    print('intentos:', i)


def operaciones(orilla_Der, orilla_izq, barca, num_rand1, num_rand2, viajes):
    print('Orilla Derecha:', orilla_Der)

    orilla_izq.append('bote')
    print('Bote va a la orilla izquierda')

    orilla_Der.append(orilla_izq[num_rand1])
    orilla_Der.append(orilla_izq[num_rand2])

    print('Orilla Izquierda:', orilla_izq)

    print('Bote aborda a:', barca)
    print('Bote va a la orilla derecha')
    del orilla_izq[orilla_izq.index(barca[0])]
    del orilla_izq[orilla_izq.index(barca[1])]

    del orilla_izq[orilla_izq.index('bote')]
    print('Orilla Izquierda actualizada:', orilla_izq)



    orilla_Der.append('bote')
    print('Orilla derecha actualizada:', orilla_Der)
    del orilla_Der[orilla_Der.index('bote')]
    # orilla_izq.append('bote')
    # time.sleep(1)  # Esta en segundos
    barca = []
    print('Bote desembarca:', barca)
    viajes += 1

    return orilla_Der, orilla_izq, barca, viajes

def comprobar_cant_canibales_misioneros_izquierda(orilla_izq):
    lista_aux_canibales = [elemento for elemento in orilla_izq if 'c' in elemento]
    lista_aux_misioneros = [elemento for elemento in orilla_izq if 'm' in elemento]
    num_canibales = len(lista_aux_canibales)
    num_misioneros = len(lista_aux_misioneros)
    return num_canibales, num_misioneros

def comprobar_cant_canibales_misioneros_derecha(orilla_Der):
    lista_aux_canibales = [elemento for elemento in orilla_Der if 'c' in elemento]
    lista_aux_misioneros = [elemento for elemento in orilla_Der if 'm' in elemento]
    num_canibales = len(lista_aux_canibales)
    num_misioneros = len(lista_aux_misioneros)
    return num_canibales, num_misioneros

def restablecer(orilla_izq, orilla_Der, barca):
    orilla_izq = canibales + misioneros
    orilla_Der = []
    barca = []
    return orilla_izq, orilla_Der, barca

canibales = ['c1', 'c2', 'c3']
misioneros = ['m1', 'm2', 'm3']
busqueda_fuerza_bruta_aleatoria(canibales, misioneros)
