# Escribir una función encontrar_2 que reciba por parámetro dos cadenas: 
# cadena y subcadena. Retornar la posición de la subcadena si esta se encuentra 
# dentro de la cadena y -1 si no se encuentra. No usar find().

# Ejemplo: si los argumentos son “abbbccda” y “bbc” entonces se retorna 2.

cadena = "abbbccda"
subcadena = "bbc"

def encontrar(cadena, subcadena):
    i = 0
    while i<= len(cadena) - len(subcadena):
        if cadena[i:i+len(subcadena)] == subcadena:
            return i
        i += 1
    return -1

print(encontrar("abbbccda","bbc"))