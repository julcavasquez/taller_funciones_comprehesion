#Plantear 2 formas de encontrar los números comunes entre 2 listas sin usar set.
lista1 = [1,2,3,4,5,6,7]
lista2 = [4,5,6,7,8,9,10]
comunes = []

for n1 in lista1:
    for n2 in lista2:
        if (n1 == n2) and (n1 not in comunes):
            comunes.append(n1)

print(f"Los números comunes son => {comunes}")