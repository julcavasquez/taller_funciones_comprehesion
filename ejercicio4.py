# Para los números entre 10 y 500, expresar en un diccionario el número y su respectivo 
# dígito más alto por el cuál es divisible. Por ejemplo para 328 es 8.

#solucion 1
# lista = []
# diccionario = {}
# for i in range(10,501):
#     divisores = []
#     for j in range(1,9):
#         if i % j == 0:
#             divisores.append(j)
#     diccionario[i]=max(divisores)
# print(diccionario)
# #solucion 2
# datos = {i:j for j in range(326,501) for j in range(1,10) if i % j == 0}
# print(datos)

lista = [numero for numero in 
            [[j for i in range(10,13)] for j in range(1,10) if i % j == 0]]
print(lista)