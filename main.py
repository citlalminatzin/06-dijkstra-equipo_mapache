#!/usr/bin/env python
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

def minimal_distance(M: list[list[float]], origin:int, destination:int)-> float:
    """Devuelve la distancia mínima entre el origin y destination"""

    resultados = dijkstra(M, origin)
    distancias = resultados[0]
    return distancias[destination]

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
    los vértices entre sí
    """
    M1 = grafica_1() 
    n = len(M1)
    distancias = [dijkstra(M1, i) for i in range(n)]
    return distancias

def ejercicio_3b():
    M2 = grafica_2()
    n = len(M2)
    distancias = [dijkstra(M2, i) for i in range(n)]
    return distancias
    
def ejercicio_3c():
    M3 = grafica_3()
    n = len(M3)
    return [dijkstra(M3, i) for i in range(n)]

def ejercicio_4():
    M4 = grafica_4()
    n = len(M4)
    return [minimal_distance(M4,0,11)]

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

def main():
    #Ejercicio 1
    print("\nEjercicio 1")
    print("\n" + "-"*20)
    ej1 = ejercicio_1()
    print(f"Nodo inicial: 0")
    print(f"Distancias finales (D): {ej1[0]}")
    print(f"Predecesores (P): {ej1[1]}")

    #Ejercicio 2
    print("\nEjercicio 2")
    print("\n" + "-"*20)
    origen =0
    destino=2

    distancias, predecesores= ej1
    camino = cam_opt(predecesores, origen, destino)

    if camino:
        print(f"Camino óptimo de {origen} a {destino}:",
              " → ".join(map(str, camino)))
        print("Distancia:", distancias[destino])
    else:
        print("No hay camino")

    #Ejercicio 3
    print("\nEjercicio 3:")
    print("\n" + "-"*20)
    print("\nGráfica 1")
    ej3a = ejercicio_3a()
    print(f"Distancias desde el nodo 0: {ej3a[0][0]}")
    print(f"Predecesores desde el nodo 0: {ej3a[0][1]}")

    print("\nGráfica 2")
    ej3b = ejercicio_3b()
    print(f"Distancias desde el nodo 0: {ej3b[0][0]}")
    print(f"Predecesores desde el nodo 0: {ej3b[0][1]}")

    print("\nGráfica 3")
    ej3c = ejercicio_3c()
    print(f"Distancias desde el nodo 0: {ej3c[0][0]}")
    print(f"Predecesores desde el nodo 0: {ej3c[0][1]}")

    #Ejercicio 4
    print("Ejercicio 4 ")
    print(f"Distancia mínima  {ejercicio_4()}")


if __name__ == "__main__":
    main()
