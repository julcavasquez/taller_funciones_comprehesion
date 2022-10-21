#Encontrar todos los números comprendidos entre 7 y 537 que contengan el dígito 7
lista_numeros = []

for i in range(7,538):
    for n in str(i):
        n = int(n)
        if n == 7:
            lista_numeros.append(i)
print(lista_numeros)