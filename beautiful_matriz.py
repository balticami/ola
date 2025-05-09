import sys
matriz = []
aux = 0
index = 0

datos = list(map(int, sys.stdin.read().split()))

for i in range(5):
    fila = []
    for j in range(5):
        fila.append(datos[index])
        index += 1  
    matriz.append(fila)

for i in range(len((matriz))):
    print(matriz[i])

#ok ahora a encontrar la posición del 1

for i in range(5):
    for j in range(5):
        if(matriz[i][j] == 1):
            aux = aux + abs(i-2) 
            aux = aux + abs(j-2)

print(aux)

            
    




