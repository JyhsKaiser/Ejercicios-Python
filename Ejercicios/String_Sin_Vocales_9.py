
frase = 'string sin vocales, ejercicios practicos de python'.s
frase_aux = ''
char_stop = input('Ingresa una letra: ')
vowels = 'aeiouAEIOU'
for i in range(len(frase)):
    if frase[i].lower() == char_stop.lower():
        break
    elif frase[i] not in vowels:
        frase_aux += frase[i]
print(frase_aux)
