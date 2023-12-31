# -*- coding: utf-8 -*-
"""Corriente alterna simu.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A8GFC8DYt69BLKGjoi5en21S-_FrbClh
"""

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
from sklearn.linear_model import LinearRegression
import scipy.stats as stats



import io

"""LINK COLLAB: https://colab.research.google.com/drive/1A8GFC8DYt69BLKGjoi5en21S-_FrbClh?usp=sharing

Importar desde PC
"""

from google.colab import files
uploaded = files.upload()

"""calculo w_0 teorico"""

r_0 = 25
R_l = 0
L_0 = 90/1000
C_0 = 0.01/1000000
R_t= R_l + r_0

w_0 = 1/np.sqrt(L_0 * C_0)
f_0 = w_0/ (2 * np.pi)
delta_w = R_t / L_0
Q = w_0 * (L_0 / R_t)
T = r_0/R_t
T_2 = T / np.sqrt(2)


print(T)
print(T_2)
print(f_0)
print(delta_w)
print(Q)

r_0 = 10
R_l = 40
L_0 = 90/1000
C_0 = 0.01/1000000
R_t= R_l + r_0

w_0 = 1/np.sqrt(L_0 * C_0)
f_0 = w_0/ (2 * np.pi)
delta_w = R_t / L_0
Q = w_0 * (L_0 / R_t)
T = r_0/R_t
T_2 = T / np.sqrt(2)


print(T)
print(T_2)
print(f_0)
print(delta_w)
print(Q)

"""Intento analizar los graficos de ltspice

"""

trans10 = pd.read_csv('AC - t10.csv')
x_trans10 = trans10['Freq.']
y_trans10	= trans10['V(n004)/V(n002)']

trans15 = pd.read_csv('AC - t15.csv')
x_trans15 = trans15['Freq.']
y_trans15	= trans15['V(n004)/V(n002)']

trans20 = pd.read_csv('AC - t20.csv')
x_trans20 = trans20['Freq.']
y_trans20	= trans20['V(n004)/V(n002)']

trans25 = pd.read_csv('AC - t25.csv')
x_trans25 = trans25['Freq.']
y_trans25	= trans25['V(n004)/V(n002)']

trans30 = pd.read_csv('AC - t30.csv')
x_trans30 = trans30['Freq.']
y_trans30	= trans30['V(n004)/V(n002)']

trans50 = pd.read_csv('AC - t50.csv')
x_trans50 = trans50['Freq.']
y_trans50	= trans50['V(n004)/V(n002)']

plt.rc('font', size = 17)

plt.figure(figsize=(17,6))
#plt.plot(x_trans10, y_trans10, "o", label = "R = 10")
#plt.plot(x_trans15, y_trans15, "o", label = "R = 15")
#plt.plot(x_trans20, y_trans20, "o", label = "R = 20")
#plt.plot(x_trans25, y_trans25, "o", label = "R = 25")
#plt.plot(x_trans30, y_trans30, "o", label = "R = 30")
plt.plot(x_trans50, y_trans50, "o",label = "R = 50")
plt.axvline(5305, c = 'red',  label = 'f_0')
plt.ylabel(r'Transferencia', fontsize=15)
plt.xlabel(r'f [Hz]', fontsize=15)
plt.legend(fontsize = 13)
plt.grid(linestyle='--')
plt.grid(which = 'minor',linestyle=':', linewidth='0.1', color='black' )
plt.plot

"""Pongo una resistencia a la inductancia y vario. Dejo R_0 en 10 y agrego 5, 10, 15, 20 y 40. En teoria tiene que ser lo mismo que previas medidas de transferencia."""

RL5 = pd.read_csv('AC - RL5.csv')
x_5 = RL5['Freq.']
y_5 = RL5['V(n004)/V(n001)']

RL10 = pd.read_csv('AC - RL10.csv')
x_10 = RL10['Freq.']
y_10	= RL10['V(n004)/V(n001)']

RL15 = pd.read_csv('AC - RL15.csv')
x_15 = RL15['Freq.']
y_15	= RL15['V(n004)/V(n001)']

RL20 = pd.read_csv('AC - RL20.csv')
x_20 = RL20['Freq.']
y_20	= RL20['V(n004)/V(n001)']

RL40 = pd.read_csv('AC - RL40.csv')
x_40 = RL40['Freq.']
y_40	= RL40['V(n004)/V(n001)']

plt.figure(figsize=(15,10))
#plt.plot(x_5, y_5, "o", label = "RL = 5")
#plt.plot(x_10, y_10, "o", label = "RL = 10")
#plt.plot(x_15, y_15, "o", label = "RL = 15")
#plt.plot(x_20, y_20, "o", label = "RL = 20")
plt.plot(x_40, y_40, "o", label = "RL = 40")
plt.axvline(5304, c = 'red',  label = 'f_0')
plt.ylabel(r'Transferencia', fontsize=15)
plt.xlabel(r'f [Hz]', fontsize=15)
plt.legend(fontsize = 13)
plt.grid(linestyle='--')
plt.grid(which = 'minor',linestyle=':', linewidth='0.1', color='black' )
plt.plot

plt.figure(figsize=(15,10))
plt.plot(x_40, y_40, "o", label = "RL = 5")
plt.plot(x_trans50, y_trans50, "o", label = "R = 15")
plt.axvline(5304, c = 'red',  label = 'f_0')
plt.ylabel(r'Transferencia', fontsize=15)
plt.xlabel(r'f [Hz]', fontsize=15)
plt.legend(fontsize = 13)
plt.grid(linestyle='--')
plt.grid(which = 'minor',linestyle=':', linewidth='0.1', color='black' )
plt.plot

"""Bode

"""

bode = pd.read_csv('AC - bode.csv')
x_bode = bode['Freq.']
y_bode	= bode['V(n004)/V(n002)']
z_bode = bode["C"]

plt.figure(figsize=(15,10))
plt.plot(x_bode, y_bode)
plt.ylabel(r'Potencia', fontsize=15)
plt.xlabel(r'Hz', fontsize=15)
plt.legend(fontsize = 13)
plt.grid(linestyle='--')
plt.grid(which = 'minor',linestyle=':', linewidth='0.1', color='black' )
plt.plot

x = x_bode
y = y_bode
z = z_bode


fig, ax = plt.subplots(figsize = (10,5))

fig.subplots_adjust(right=0.75)

twin1 = ax.twinx()

p1, = ax.plot(x, y, "b-", label="Transferencia")
p2, = twin1.plot(x,-z, "r-", label="Desfasaje")

ax.axhline(max(y), ls = '--', lw =2, c = '#FF00C3', label = r'$P_{MAX}$')
ax.axvline(1220, ls = '--', lw =2, c = 'purple', label = r'$R_{TH}$ ')

ax.set_xlim(min(x), max(x))
ax.set_ylim(0, max(y))
twin1.set_ylim(0, max(-z))

ax.set_xlabel(r'Resistencia $r$ [$\Omega$]',fontsize = 14)
ax.set_ylabel("Potencia [$mW$]",fontsize = 14)
twin1.set_ylabel("Corriente [$mA$]",fontsize = 14)

ax.yaxis.label.set_color(p1.get_color())
twin1.yaxis.label.set_color(p2.get_color())

tkw = dict(size=4, width=1.5)
ax.tick_params(axis='y', colors=p1.get_color(), **tkw)
twin1.tick_params(axis='y', colors=p2.get_color(), **tkw)

ax.legend()
ax.legend(handles=[p1, p2],fontsize = 14, loc = 4)
ax.grid()

plt.show()