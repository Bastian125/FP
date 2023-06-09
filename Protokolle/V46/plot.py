# Imports
import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import scipy.constants as const

# B-Feld Auswertung
x, B = np.genfromtxt('data/bfeld.txt', unpack=True)

# Plot 1
plt.plot(x, B, 'x', label='Messwerte')
plt.xlabel('$x/$mm')
plt.ylabel('$B/$mT')
plt.xlim(65, 115)
plt.ylim(0)
plt.grid()
plt.legend()

plt.tight_layout()
plt.savefig('build/plot.pdf')
plt.close()

# undotiert Auswertung
l1, a11, g11, a12, g12 = np.genfromtxt('data/undotiert.txt', unpack=True)
# Daten von Grad+Winkelminuten in Radiant umrechnen
d1 = (a11 + g11/60)*(np.pi)/180
d2 = (a12 + g12/60)*(np.pi)/180

# Differenz berechnen
ld1 = 0.5*np.abs(d1-d2)
# Normieren
dp1 = 5.1*10**(-3)
ld1_n = ld1/dp1


# als txt speichern
np.savetxt('data/winkeldiff1.txt', ld1_n)

# dotiert1 Auswertung
l2, a21, g21, a22, g22 = np.genfromtxt('data/dotiert1.txt', unpack=True)
# Daten von Grad+Winkelminuten in Radiant umrechnen
d3 = (a21 + g21/60)*(np.pi)/180
d4 = (a22 + g22/60)*(np.pi)/180

# Differenz berechnen
ld2 = 0.5*np.abs(d3-d4)

# Normieren
dp2 = 5.1*10**(-3)
ld2_n = ld2/dp2

# als txt speichern
np.savetxt('data/winkeldiff2.txt', ld2_n)

# dotiert2 Auswertung
l3, a31, g31, a32, g32 = np.genfromtxt('data/dotiert2.txt', unpack=True)
# Daten von Grad+Winkelminuten in Radiant umrechnen
d5 = (a31 + g31/60)*(np.pi)/180
d6 = (a32 + g32/60)*(np.pi)/180

# Differenz berechnen
ld3 = 0.5*np.abs(d5-d6)
# Normieren
dp3 = 5.1*10**(-3)
ld3_n = ld3/dp3

# als txt speichern
np.savetxt('data/winkeldiff3.txt', ld3_n)

# ld1 bis ld6 in Grad als txt abspeichern
np.savetxt('data/d1.txt', d1*180/np.pi)
np.savetxt('data/d2.txt', d2*180/np.pi)
np.savetxt('data/d3.txt', d3*180/np.pi)
np.savetxt('data/d4.txt', d4*180/np.pi)
np.savetxt('data/d5.txt', d5*180/np.pi)
np.savetxt('data/d6.txt', d6*180/np.pi)

# theta 1 bis 3
np.savetxt('data/theta1.txt', ld1)
np.savetxt('data/theta2.txt', ld2)
np.savetxt('data/theta3.txt', ld3)

# theta/d 1 bis 3
np.savetxt('data/thetad1.txt', ld1_n)
np.savetxt('data/thetad2.txt', ld2_n)
np.savetxt('data/thetad3.txt', ld3_n)

# Plotte theta/d gegen lambda^2
plt.plot(l1**2, ld1_n, 'x', label=r'GaAs undotiert')
plt.plot(l2**2, ld2_n, 'x', label=r'GaAs n-dotiert, $N=1,2\cdot 10^{18}\,$cm$^{-3}$')
plt.plot(l3**2, ld3_n, 'x', label=r'GaAs n-dotiert, $N=2,8\cdot 10^{18}\,$cm$^{-3}$')

plt.xlabel(r'$\lambda^2 \:/\:\mathrm{µm}^2$')
plt.ylabel(r'$\frac{\Theta}{d} \:/\:$rad$\mathrm{m}^{-1}}$')
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('build/plot1.pdf')
plt.close()

# Differenz plotten

# Lineare Regression 1
params, covariance_matrix = np.polyfit(l1**2, ld2_n - ld1_n, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')

# Lineare Regression 2
params1, covariance_matrix1 = np.polyfit(l1**2, ld3_n - ld1_n, deg=1, cov=True)

errors1 = np.sqrt(np.diag(covariance_matrix1))

for name, value, error in zip('ab', params1, errors1):
    print(f'{name} = {value:.3f} ± {error:.3f}')

# Plot

plt.plot(l1**2, ld2_n - ld1_n, 'x', label=r'GaAs n-dotiert, $N=1,2\cdot 10^{18}\,cm^{-3}$')
plt.plot(l1**2, ld3_n - ld1_n, 'x', label=r'GaAs n-dotiert, $N=2,8\cdot 10^{18}\,cm^{-3}$')
plt.plot(
    l1**2,
    params[0] * l1**2 + params[1], 'b-',
    label=r'Lineare Regression, $N=1,2\cdot 10^{18}\,cm^{-3}$',
    linewidth=2,
)
plt.plot(
    l1**2,
    params1[0] * l1**2 + params1[1], color='orange',
    label=r'Lineare Regression, $N=2,8\cdot 10^{18}\,cm^{-3}$',
    linewidth=2,
)
plt.xlabel(r'$\lambda^2 \:/\:\mathrm{µm}^2$')
plt.ylabel(r'$\frac{\Theta}{d} \:/\:$rad$\mathrm{m}^{-1}}$')

plt.grid()
plt.legend()
plt.savefig('build/plot2.pdf')
plt.close()

#freie Massen bestimmen
a1 = ufloat(5264638028593.00, 906926335419.09)
a2 = ufloat(2480202027226.74, 711670873463.99)
B = 422e-3
N1 = (1.2*10**(12))/(10**(-2))**3
N2 = (2.8*10**(12))/(10**(-2))**3
n = 3.3543

def get_m(a, N):
    return ((const.e**(3)*N*B)/(8*const.pi**(2)*const.c**(3)*const.epsilon_0*n*a))**(0.5)

m_t = 0.063
m1 = get_m(a1, N1)
m2 = get_m(a2, N2)
m_1 = m1/const.electron_mass
m_2 = m2/const.electron_mass
m = 0.5*(m1+m2)

print('m_1 = ', m1)
print('m_2 = ', m2)
print('m_1/m_e = ', m_1)
print('m_2/m_e = ', m_2)
print('m/m_e = ', m/const.electron_mass)
print('Abweichung m_1', 100*(m_1 - m_t)/m_t, '%')
print('Abweichung m_2', 100*(m_2 - m_t)/m_t, '%')
print('Abweichung m', 100*(m/const.electron_mass - m_t)/m_t, '%')