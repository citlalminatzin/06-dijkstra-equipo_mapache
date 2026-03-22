#!/usr/bin/env python

import numpy as np
import pandas as pd 

def read_data(path="data/distances.csv"):
    """Lee los datos de un csv y te los devuelve"""
    # Por ahora, como estamos trabajando con matrices de la práctica:
    return np.genfromtxt(path, delimiter=',')

def get_grafica_1():
    """Matriz de pesos. Gráfica 1"""
    M1 = np.zeros((8,8))
    M1[0,1] = M1[1,0] = 3
    M1[1,2] = M1[2,1] = 1
    M1[0,3] = M1[3,0] = 2
    M1[3,2] = M1[2,3] = 3
    M1[1,4] = M1[4,1] = 4
    M1[2,5] = M1[5,2] = 2
    M1[2,6] = M1[6,2] = 2
    M1[3,6] = M1[6,3] = 4
    M1[4,7] = M1[7,4] = 6
    M1[5,7] = M1[7,5] = 4
    M1[5,6] = M1[6,5] = 3
    M1[6,7] = M1[7,6] = 5
    return M1

def get_grafica_2():
    """Matriz de pesos. Gráfica 2"""
    M2 = np.zeros((4,4))
    M2[0,1] = 9
    M2[3,2] = 2
    M2[0,3] = 6
    M2[1,3] = 1
    M2[2,1] = 3
    return M2

def get_grafica_3():
    """Matriz de pesos. Gráfica 3"""
    M3 = np.zeros((4,4))
    M3[0,1] = 4
    M3[0,2] = 8
    M3[0,3] = 16
    M3[1,2] = 5
    M3[1,3] = 11
    M3[2,3] = 6
    return M3
if __name__ == "__main__":
    main()
