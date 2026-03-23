#!/usr/bin/env python
import dijkstra
import data
def main():
    #Ejercicio 1
    print("\nEjercicio 1")
    print("\n" + "-"*20)
    ej1 = dijkstra.ejercicio_1()
    print(f"Nodo inicial: 0")
    print(f"Distancias finales (D): {ej1[0]}")
    print(f"Predecesores (P): {ej1[1]}")

    #Ejercicio 2
    print("\nEjercicio 2")
    print("\n" + "-"*20)
    origen =0
    destino=2

    distancias, predecesores= ej1
    camino = dijkstra.cam_opt(predecesores, origen, destino)

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
    ej3a = dijkstra.ejercicio_3a()
    print(f"Distancias desde el nodo 0: {ej3a[0][0]}")
    print(f"Predecesores desde el nodo 0: {ej3a[0][1]}")

    print("\nGráfica 2")
    ej3b = dijkstra.ejercicio_3b()
    print(f"Distancias desde el nodo 0: {ej3b[0][0]}")
    print(f"Predecesores desde el nodo 0: {ej3b[0][1]}")

    print("\nGráfica 3")
    ej3c = dijkstra.ejercicio_3c()
    print(f"Distancias desde el nodo 0: {ej3c[0][0]}")
    print(f"Predecesores desde el nodo 0: {ej3c[0][1]}")
    
    # Ejercicio 4
    print("\nEjercicio 4")
    print("\n" + "-"*20)
    M4 = data.grafica_4()
    distancias, predecesores = dijkstra.dijkstra(M4, 0)
    print("Distancias desde el nodo 0:")
    print(distancias)
    print("\nPredecesores:")
    print(predecesores)

    origen = 0     
    destino = 11   

    camino = dijkstra.cam_opt(predecesores, origen, destino)

    if camino:
        camino_visual = [n + 1 for n in camino]

        print(f"\n Camino con la distancia mínima de 1 a 12:",
            " → ".join(map(str, camino_visual)))
        print("Distancia:", distancias[destino])
    else:
        print("No hay camino")

if __name__ == "__main__":
        main()
