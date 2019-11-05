# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 00:10:16 2019

@author: Ayush RKL
"""
import pandas as pd
import numpy as np

f = pd.read_csv("3D_spatial_network.txt", header = None, delimiter = ',')
f1 = open("cost_values.txt", 'w+')

a = np.zeros([3, 3])
b = np.zeros([3, 1])


n = len(f[1])
for i in range(n):
    """updating values of row1 of 'a' matrix"""
    a[0][0] += f[1][i]**2
    a[0][1] += f[1][i]*f[2][i]
    a[0][2] += f[1][i]
    
    a[1][0] += f[1][i]*f[2][i]
    a[1][1] += f[2][i]**2
    a[1][2] += f[2][i]
    
    a[2][0] += f[1][i]
    a[2][1] += f[2][i]
    
    b[0][0] += f[3][i]*f[1][i]
    b[1][0] += f[3][i]*f[2][i]
    b[2][0] += f[3][i]
    
a[2][2] = 1
print(a)
print(b)

c = np.linalg.inv(a)
print(c)
w = np.dot(c, b)
print(w)