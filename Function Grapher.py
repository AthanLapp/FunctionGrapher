"""
title:Function Grapher
Author: Athan Lapp
description: Function Grapher with set range and discretization
"""

import matplotlib.pyplot as plt

#solving the function1/2x^3+3x^2-2x+2 as an example. You can change the values disc, rnge and the function in line 22 to solve your's
disc=100  #precision 0.001 (disc-<discretization=1/precision),
x=[]
i=0
rnge=100 #x from -rnge to rnge 
for i in range(-rnge,rnge+1):
    j=0
    for j in range(i,i+disc):
        x.append(i+j/disc) #(with 1/disc step)
y=[]
for i in x:
    y.append(1/2*i**3+3*i**2-2*i+2)
plt.plot(x,y)
plt.ylabel('1/2*i**3+3*i**2-2*i+2') #Here is the function to be solved. Change it with yours
plt.show()
