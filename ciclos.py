# Ciclos
""" 
for in
while

"""
numeros = [1, 2, 3, 4]

# imprimir los numeros del 1 al 10
for i in range(1, 11): # range(start=0, stop=10, step=1)
    print(i)
    
    
for i in range(len(numeros)):
    print(numeros[i]) # 1 2 3
    
for numero in numeros:
    print(numero)


indice = 0
while indice < len(numeros):
    print(numeros[indice])
    indice+=1
    #indice = indice + 1