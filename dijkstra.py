import matplotlib.pyplot as plt
import numpy as np 
from math import inf

def create_adjacency_matrix()->list[list[float]]:
    """
    Crea una matriz de adyacencia
    """
    ...

def dijkstra(M: list[list[float]], origin: int) -> list[list[float]]:
    """
    M : Matriz de pesos de una gráfica
    origin: índice del nodo inicial

    returns
    lista con las distancia de las rutas y el origen de la arista
    con la que terminó la ruta
    """
    n= len(M)
    # ---
    # Paso 1: Inicializa las distancias
    # ---
    distancias = [inf] * n
    distancias[origin] = 0
    predecesores = [None] * n
    permanentes = [False] * n

    for _ in range(n):
        
    # ---
    # Paso 2: Marca el nodo permanente
    # ---    
        u = -1
        menor_distancia = inf
        for i in range(n):
            if not permanentes[i] and distancias[i] < menor_distancia:
                menor_distancia = distancias[i]
                u = i
        
        if u == -1 or distancias[u] == inf:
            break
            
        permanentes[u] = True
   
    # ---
    # Paso 3: Identifica los nodos vecinos disponibles
    # ---
        for v in range(n):
           
            if M[u][v] > 0 and not permanentes[v]:
                distancia_temporal = distancias[u] + M[u][v]
    
    # ---
    # Paso 4: Reetiquetado
    # ---
                if distancia_temporal < distancias[v]:
                    distancias[v] = distancia_temporal
                    predecesores[v] = u

    # ---
    # Paso 5: Actualizar el nodo permanente
    # ---
    """Cuando el for se reinicia, este paso sucede."""
    distancias = [float(x) for x in distancias]
    return [distancias, predecesores]

#Funcion para la distancia mínima 
def minimal_distance(M: list[list[float]], origin:int, destination:int)-> float:
    """Devuelve la distancia mínima entre el origen y destino"""

    resultados = dijkstra(M, origin)
    distancias = resultados[0]
    return distancias[destination]

#Función:Camino optimo
def cam_opt(predecesores, origen, destino):
    camino = []
    actual = destino

    while actual is not None:
        camino.append(actual)
        actual = predecesores[actual]

    camino.reverse()
    if camino[0] != origen:
        return None

    return camino

def ejercicio_1():
    """
    Regresa las distancias mínimas del
    primer vértice a todos los demás
    """
    MD = grafica_1()
    n = len(MD)
    return dijkstra(MD, 0)

def ejercicio_3a():
    """
    Regresa las distancias mínimas de todos
    los vértices de la grafica 1 entre sí
    """
    M1 = grafica_1() 
    n = len(M1)
    distancias = [dijkstra(M1, i) for i in range(n)]
    return distancias

def ejercicio_3b():
    """
    Regresa las distancias mínimas de todos
    los vértices de la grafica 2 entre sí
    """
    M2 = grafica_2()
    n = len(M2)
    distancias = [dijkstra(M2, i) for i in range(n)]
    return distancias
    
def ejercicio_3c():
    """
    Regresa las distancias mínimas de todos
    los vértices de la grafica 3 entre sí
    """
    M3 = grafica_3()
    n = len(M3)
    return [dijkstra(M3, i) for i in range(n)]

def ejercicio_4():
    M4 = grafica_4()
    n = len(M4)
    return [minimal_distance(M4,0,11)]