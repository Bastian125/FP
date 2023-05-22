import matplotlib.pyplot as plt
import numpy as np
import uncertainties as unp
from scipy import stats
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)

## TEM Moden:

d, I01, I00 = np.genfromtxt('content/data/moden.txt', unpack=True)

I00 = I00 - 0.13 #background
I01 = I01 - 0.13 #background

def model1(x, I0, x0, w):
    return I0 * np.exp(-(x-x0)**2/(2*w**2))

parameters1, pcov1 = curve_fit(model1, d , I00, sigma=None)
I0 =unp.uarray(parameters1[0],pcov1[0,0])
x0_1 =unp.uarray(parameters1[1],pcov1[1,1])
w_1 =unp.uarray(parameters1[2],pcov1[2,2])
print("Fit TEM00:")
print(f"I0={I0}")
print(f"x0={x0_1}")
print(f"w={w_1}")
print("\n")

plt.scatter(d, I00, label='Messwerte', marker ="x", color = "red")
x = np.linspace(-10,10,1000)
plt.plot(x,model1(x, *parameters1), label="Fit")
plt.xlabel(r'$d \,/\,\unit{\milli\metre}$')
plt.ylabel(r'$I \,/\,\unit{\micro\watt}$')
plt.legend(loc='best')
plt.grid()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot_TEM00.pdf')
plt.close()

def model2(x, I1, x0, x1, w):
    return I1 * (8*(x-x0)**2/w**2) * np.exp(-(x-x1)**2/(2*w**2))

parameters2, pcov2 = curve_fit(model2, d , I01, sigma=None)
I1 =unp.uarray(parameters2[0],pcov2[0,0])
x0_2 =unp.uarray(parameters2[1],pcov2[1,1])
x1 =unp.uarray(parameters2[2],pcov2[2,2])
w_2 =unp.uarray(parameters2[3],pcov2[3,3])
print("Fit TEM01:")
print(f"I1={I1}")
print(f"x0={x0_2}")
print(f"x1={x1}")
print(f"w={w_2}")
print("\n")

plt.scatter(d, I01, label='Messwerte', marker ="x", color = "red")
plt.plot(x,model2(x, *parameters2), label="Fit")
plt.xlabel(r'$d \,/\,\unit{\milli\metre}$')
plt.ylabel(r'$I \,/\,\unit{\micro\watt}$')
plt.legend(loc='best')
plt.grid()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot_TEM01.pdf')
plt.close()


## Polarisation

phi, I = np.genfromtxt('content/data/polarisation.txt', unpack=True)

I = I - 0.02 #background

def model3(x, I, phi0):
    return I * (np.sin(np.radians(x)-phi0))**2

parameters3, pcov3 = curve_fit(model3, phi , I, sigma=None)
I_ =unp.uarray(parameters3[0],pcov3[0,0])
phi_0 =unp.uarray(np.degrees(parameters3[1]),np.degrees(pcov3[1,1]))
print("Fit Polarisation:")
print(f"I={I_}")
print(f"phi0={phi_0}")
print("\n")

plt.scatter(phi, I, label='Messwerte', marker ="x", color = "red")
xx = np.linspace(0,360,1000)
plt.plot(xx,model3(xx, *parameters3), label="Fit")
plt.xlabel(r'$\phi \,/\,\unit{\degree}$')
plt.ylabel(r'$I \,/\,\unit{\milli\watt}$')
plt.legend(loc='best')
plt.grid()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot_pol.pdf')
plt.close()

## Frequenzbreite

## Wellenlänge

n, g, d, s1, s2, s3, s4 = np.genfromtxt('content/data/beugung.txt', unpack=True)

def Lambda(n,g,s,d):
    return (g**-1/n) * np.sin( np.arctan(s/(2*d)) )

lambda1= np.zeros(4)
for i in range(4):
    lambda1[i] = Lambda(n[i], g[0], s1[i], d[0])

lambda2= np.zeros(4)
for i in range(4):
    lambda2[i] = Lambda(n[i], g[1], s2[i], d[1])

lambda3= np.zeros(2)
for i in range(2):
    lambda3[i] = Lambda(n[i], g[2], s3[i], d[2])

lambda4= 0
lambda4 = Lambda(n[0], g[3], s4[0], d[3])

lambda1= lambda1*10**6 ## in nm
lambda2= lambda2*10**6 ## in nm
lambda3= lambda3*10**6 ## in nm
lambda4= lambda4*10**6 ## in nm

print("Wellenlängen:")
print(f" 1. Gitter: {lambda1} nm")
print(f" 2. Gitter: {lambda2} nm")
print(f" 3. Gitter: {lambda3} nm")
print(f" 4. Gitter: {lambda4} nm")
print("\n")

lambda1234 = np.concatenate((lambda1, lambda2, lambda3, lambda4), axis=None)
lambda_tot = unp.uarray(np.mean(lambda1234),np.std(lambda1234))
print(f"Mittelwert Lambda: {lambda_tot} nm")