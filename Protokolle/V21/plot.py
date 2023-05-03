import matplotlib.pyplot as plt
import numpy as np

import uncertainties as unp
from scipy import stats
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)
import scipy.constants as const


f, U1, I1, U2, I2 = np.genfromtxt('content/data.txt', unpack = True)

N_sweep = 11
R_sweep = 16.39*10**-2

N_hor = 154
R_hor = 15.79*10**-2

f = f*1000
I_sweep1 = U1 * 0.1
I_sweep2 = U2 * 0.1

I1 = I1/1000
I2 = I2/1000

def B_Feld(N,I,R):
    return(const.mu_0*(8*N*I)/(np.sqrt(125)*R))


B_Feld_1 = B_Feld(N_sweep, I_sweep1, R_sweep) + B_Feld(N_hor, I1, R_hor)

B_Feld_2 = B_Feld(N_sweep, I_sweep2, R_sweep) + B_Feld(N_hor, I2, R_hor)

m1 , b1 , r1 ,p1 ,m1_err = stats.linregress(f,B_Feld_1)
m2 , b2 , r2 ,p2 ,m2_err = stats.linregress(f,B_Feld_2)

def FehlerB(x,m_err):
    b_err=m_err*(sum(x**2)/len(x))**(1/2)
    return b_err

M1 = unp.uarray(m1,m1_err)
B1 = unp.uarray(b1,FehlerB(f,m1_err))

M2 = unp.uarray(m2,m2_err)
B2 = unp.uarray(b2,FehlerB(f,m2_err))

# plots:

plt.scatter(f/1000, B_Feld_1*10**6, label='Isotop 1', marker ="x")
plt.plot(f/1000,((m1*f+b1)*10**6), label="Regression 1")
plt.scatter(f/1000, B_Feld_2*10**6, label='Isotop 2', marker ="x")
plt.plot(f/1000,((m2*f+b2)*10**6), label="Regression 2")
plt.xlabel(r'$f \,/\,\unit{\kilo\hertz}$')
plt.ylabel(r'$B \,/\,\unit{\micro\tesla}$')
plt.legend(loc='best')
plt.grid()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')

# fit result:

print(f"M1: {M1}, B1: {B1}")
print(f"M1: {M2}, B1: {B2}")

# g-Faktor:

mu_b = (const.e*const.hbar)/(2*const.m_e)

g_F1 = (const.h)/(mu_b*M1)

g_F2 = (const.h)/(mu_b*M2)

print(f"Erster g_Faktor:{g_F1}")
print(f"Zweiter g_Faktor:{g_F2}")

# Kernspin:

S = 1/2
L = 0
J = L+S

g_j = (3.0023 * (J**2 + J) + 1.0023 * ((S**2 + S) - (L**2 + L))) / (2 * (J**2 + J))

I1 = g_j / (4 * g_F1) - 1 + unp.sqrt((g_j / (4 * g_F1) - 1)**2+ 3 * g_j / (4 * g_F1) - 3 / 4)
I2 = g_j / (4 * g_F2) - 1 + unp.sqrt((g_j / (4 * g_F2) - 1)**2+ 3 * g_j / (4 * g_F2) - 3 / 4)

print(f"Erster Kernspin: I1={I1}")
print(f"Zweiter Kernspin: I2={I2}")