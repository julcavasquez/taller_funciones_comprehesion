
# Escribir una función imprime_lista_anidada_1 para imprimir listas anidadas. 
# Cada sublista debe ser impresa en una línea diferente. Los elementos dentro de 
# la sublista deben estar separados por una tabulación. No use índices. 
# Si el argumento es [[1,2,3],[4,5],[6,7,8,9]], la función debe imprimir:

# 1 2 3 4 5 6 7 8 9

a = [[1,2,3],[4,5],[6,7,8,9]]

def imprimir(l):
    for s in l:
        for e in s:
            print(e, end='\t')
    print(end = '\n')
imprimir(a)