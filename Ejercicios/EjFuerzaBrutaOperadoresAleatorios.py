'''
¿Qué es la Búsqueda por Fuerza Bruta con Operadores Aleatorios?
La búsqueda por fuerza bruta con operadores aleatorios es una técnica de optimización que explora el espacio
de soluciones de un problema de manera aleatoria. A diferencia de la búsqueda por fuerza bruta tradicional,
que revisa sistemáticamente todas las posibles soluciones, este enfoque genera soluciones candidatas de forma
aleatoria, lo que puede ser útil cuando el espacio de búsqueda es demasiado grande para ser explorado por completo.
Es un algoritmo metaheurístico.
'''
import random
from importlib.util import source_hash


def busqueda_fuerza_bruta_aleatoria(lista_numeros):
    """
    Realiza una búsqueda aleatoria para encontrar el valor máximo en una lista.

    Args:
      lista_numeros: Una lista de números enteros.

    Returns:
      El valor máximo encontrado y el número de intentos realizados.
    """
    if not lista_numeros:
        return None, 0

    mejor_solucion = -float('inf')  # Inicializamos con un valor muy pequeño
    intentos = 0
    indices = []

    while True:
        # Seleccionamos un índice aleatorio
        indice_aleatorio = random.randint(0, len(lista_numeros) - 1)

        if not indice_aleatorio in indices:
            indices.append(indice_aleatorio)

            # Obtenemos la solución candidata
            solucion_candidata = lista_numeros[indice_aleatorio]
            # Comparamos con la mejor solución encontrada hasta ahora
            if solucion_candidata > mejor_solucion:
                mejor_solucion = solucion_candidata

            intentos += 1
        else:
            intentos += 1
            continue
        if len(indices) == len(lista_numeros):
            break
    return mejor_solucion, intentos


# Ejemplo de uso
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
valor_maximo, num_intentos = busqueda_fuerza_bruta_aleatoria(mi_lista)

print(f"La lista a buscar es: {mi_lista}")
print(f"El valor máximo encontrado es: {valor_maximo}")
print(f"Número de intentos realizados: {num_intentos}")
