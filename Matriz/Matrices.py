import random

def llenar_matriz(n):
    matriz = []

    for f in range(n):
        fila = []
        for c in range(n):
            fila.append(random.randint(1,10))
        
        matriz.append(fila)

    return matriz


def buscar_secuencia_fila(matriz):
    post_fila = -1
    
    for f in range(len(matriz)):
        post_columna = -1
        lista_horizontal = []
        for c in range(len(matriz)):
            lista_horizontal.append(matriz[f][c])
        
        post_fila = f
        post_columna = secuencia(lista_horizontal)
        if post_columna < 0:
            post_fila = -1
        else:
            break
    return [post_fila,post_columna],[post_fila,post_columna+3]


def buscar_secuencia_columna(matriz):
    post_fila = -1
    
    for f in range(len(matriz)):
        post_columna = -1
        lista_vertical = []
        for c in range(len(matriz)):
            lista_vertical.append(matriz[c][f])
        
        post_fila = f
        post_columna = secuencia(lista_vertical)
        if post_columna < 0:
            post_fila = -1
        else:
            break
    return [post_columna,post_fila],[post_columna+3,post_fila]

def buscar_posicion_matriz(matriz):
    secuencia = buscar_secuencia_columna(matriz)
    if secuencia[0][0] != -1 and secuencia[0][1] != -1:
        return secuencia
    secuencia = buscar_secuencia_fila(matriz)
    if secuencia[0][0] != -1 and secuencia[0][1] != -1:
        return secuencia
    


def secuencia(lista):
    listseq = []
    post = -1
    for i in range(len(lista)-1) :
        if lista[i] == lista[i+1] - 1: 
            if post == -1:
                post = i
            listseq.append(lista[i])
            listseq.append(lista[i+1])
        elif len(listseq) > 0 and len(listseq) < 4: 
            listseq = []

    listseq = set(listseq)
    if len(listseq) >= 4:
        return post
    else:
        return -1
    

A = llenar_matriz(5)
print(A)
print(buscar_posicion_matriz(A))

