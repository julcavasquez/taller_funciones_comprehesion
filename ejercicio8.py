from unittest import removeResult


l = [[1, 3], [5, 7], [1, 11], [1, 15, 7], [5, 6, 21]] 
n = 1 

def contar(l,n):
    c = 0
    for r in l:
        for e in r:
            if e == n:
                c +=1
    return c

print(contar(l,1))