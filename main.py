#!/usr/bin/env python
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
