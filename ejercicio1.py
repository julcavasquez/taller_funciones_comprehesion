#Contar el número de espacio en un string dado.
def contar_espacios(cadena): 
    count = 0
         
    for i in range(len(cadena)): 
       if cadena[i] == " ": 
            count += 1
          
    return count 

texto = "Hola mi nomnre es Jose Andersson"
print("Número de espacios es: ",contar_espacios(texto))


s = "Hola mundo bla bla bla"

a = [l for l in s if l == ' ']
print(len(a))
# c = 0
# for l in s:
#     if l == ' ':
#         c += 1
# print(c)