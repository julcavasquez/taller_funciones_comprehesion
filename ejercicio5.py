# Escribir una función extrae_columna_n que reciba como parámetro una lista M y un valor n. 
# La función debe extraer los valores "de la columna" n específica a la lista anidada dada. 
# La función debe verificar que n esté en el rango permitido. Caso contrario, la función debe
# retornar una lista vacía.

# Ejemplo:

# M = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]

# n = 0

# Para extrae_column_n(M, n) la función retornará [1, 2, 1]

M = [[1,2,3],[2,4,5],[1,1,1]]
n = 1
valore = []
def extraer_columna(M,n):
    if n <= len(M):
        for i in range(len(M)):
            if i == n:
                print(f"Lista Obtenida => {M[i]}")
    else:
        print("Rango fuera del limite")
      

extraer_columna(M,n)