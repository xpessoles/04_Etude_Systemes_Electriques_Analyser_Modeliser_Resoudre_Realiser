# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 22:23:15 2014

@author: Xavier Pessoles
"""
import matplotlib.pyplot as plt
import numpy as np
#plt.close(all)

a=-pi
b=pi
x=linspace(a,b,200)

#plt.plot(x,4*x/pi)

R0=10
R = 2.5
#plt.plot(x,R0*(9-(4*x*x/(pi*pi)))/12)

plt.plot(x,(5*R0+4*R0*(1-x*x/(pi*pi)))/24)

plt.ylabel("Evolution de la résistance (en $\Omega$)")
plt.xlabel("Angle $\\alpha$ (en radians)")
plt.grid()