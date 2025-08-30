import random
import time


def busqueda_fuerza_bruta_aleatoria(canibales, misioneros):

    mejor_solucion = []
    barca = []
    i = 0
    orilla_izq = canibales + misioneros
    orilla_Der = []
    print('Orilla Izquierda:', orilla_izq)
    print('Orilla Derecha:', orilla_Der)


    while True:
        num_rand1 = random.randint(0, len(orilla_izq) - 1)
        num_rand2 = random.randint(0, len(orilla_izq) - 1)
        if num_rand1 != num_rand2:
            i += 1
            barca.append(orilla_izq[num_rand1])
            barca.append(orilla_izq[num_rand2])


            if barca[0] in orilla_izq:
                print("--------------------------------------")
                print('Barca:', barca)
                if barca[0] in canibales and barca[1] in misioneros:
                    orilla_Der.append(barca[0])
                    orilla_Der.append(barca[1])
                elif barca[0] in misioneros and barca[1] in canibales:
                    orilla_Der.append(barca[0])
                    orilla_Der.append(barca[1])
                orilla_Der.append(orilla_izq[num_rand1])
                orilla_Der.append(orilla_izq[num_rand2])
                print('Orilla derecha actualizada:', orilla_Der)
                barca = []
                print('Barca actualizada:', barca)


                # if len(orilla_izq) == 2:
                #     orilla_izq = []
                del orilla_izq[num_rand1]
                del orilla_izq[num_rand2 - 1]
                print('Orilla Izquierda actualizada:', orilla_izq)
                time.sleep(1) # Esta en segundos

                if len(orilla_izq) == 0:
                    break
    print("--------------------------------------")
    print('intentos:',i)




    # if:
    #     print('va bien')


canibales = ['c1', 'c2', 'c3']
misioneros = ['m1', 'm2', 'm3']
busqueda_fuerza_bruta_aleatoria(canibales, misioneros)
