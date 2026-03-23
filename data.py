#!/usr/bin/env python

import numpy as np

def read_data(path="data/distances.csv"):
    """Lee los datos de un csv y te los devuelve"""
    # Por ahora, como estamos trabajando con matrices de la práctica:
    return np.genfromtxt(path, delimiter=',')

def grafica_4():
    """Matriz de pesos. Gráfica 4"""
    n=12
    M4 = np.zeros((n,n))
    M4[0,1] = 9
    M4[0,2] = 7
    M4[0,3] = 3
    M4[0,4] = 2
    M4[1,5] = 4
    M4[1,6] = 2
    M4[3,5] = 2
    M4[2,6] = 3
    M4[3,7] = 11
    M4[4,6] = 11
    M4[4,7] = 8
    M4[5,8] = 6
    M4[5,9] = 4 
    M4[6,8] = 4
    M4[6,9] = 3
    M4[7,9] = 5
    M4[7,10] = 6
    M4[8,11] = 4
    M4[9,11] = 6
    M4[10,11] = 6

    return M4


def grafica_1():
    n = 4
    MD = zeros((n, n))
    MD[0,1] = 9
    MD[3,2] = 2
    MD[0,3] = 6
    MD[1,3] = 1
    MD[2,1] = 3

    return MD

def grafica_2():
    n = 8
    M1 = zeros((n,n))

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

def grafica_3():
    n = 4
    M3 = zeros((n,n))

    M3[0,1] = 4
    M3[0,2] = 8
    M3[0,3] = 16
    M3[1,2] = 5
    M3[1,3] = 11
    M3[2,3] = 6
    
    return M3
    

