# El Problema: Contador de Palabras y Frecuencia
# Objetivo: Escribe un programa que pida al usuario que ingrese una frase o un párrafo. El programa debe hacer lo siguiente:
#
# Contar el número total de palabras.
#
# Contar la frecuencia de cada palabra (cuántas veces se repite cada una).
#
# Ignorar mayúsculas y minúsculas (por ejemplo, "Python" y "python" deben ser contadas como la misma palabra).
#
# Ignorar la puntuación (por ejemplo, comas, puntos, etc.).

def contador_palabras():
    """
    Este programa cuenta el número total de palabras y la frecuencia de cada una
    en una frase o párrafo dado por el usuario.
    """

    # 1. Obtener la entrada del usuario
    texto = input("Ingresa una frase o un párrafo: ")

    # 2. Normalizar el texto: convertir a minúsculas y quitar puntuación
    texto_normalizado = texto.lower()

    # Lista de caracteres de puntuación a eliminar
    puntuacion = '.,;?!'
    for caracter in puntuacion:
        texto_normalizado = texto_normalizado.replace(caracter, '')

    # 3. Dividir el texto en una lista de palabras
    # Usamos .split() que divide por espacios y maneja múltiples espacios
    palabras = texto_normalizado.split()

    # 4. Contar el número total de palabras
    total_palabras = len(palabras)

    # 5. Contar la frecuencia de cada palabra usando un diccionario
    frecuencia_palabras = {}
    for palabra in palabras:
        frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1

    # 6. Mostrar los resultados
    print("\n--- Resultados del análisis ---")
    print(f"Número total de palabras: {total_palabras}")

    print("\nFrecuencia de cada palabra:")
    for palabra, conteo in frecuencia_palabras.items():
        print(f"  - '{palabra}': {conteo} vez(ces)")


# Llamar a la función para ejecutar el programa
contador_palabras()