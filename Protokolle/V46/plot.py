# Imports
import matplotlib.pyplot as plt
import numpy as np

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

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot1.pdf')
plt.close()

# undotiert Auswertung
l1, a11, g11, a12, g12 = np.genfromtxt('data/undotiert.txt', unpack=True)
# Daten von Grad+Winkelminuten in Radiant umrechnen
d1 = (a11 + g11/60)*(np.pi)/180
d2 = (a12 + g12/60)*(np.pi)/180

# Differenz berechnen
ld1 = np.abs(d1-d2)
# Normieren
d1 = 5.1*10**(-3)
ld1_n = ld1/d1

# als txt speichern
np.savetxt('data/winkeldiff1.txt', ld1_n)

# dotiert1 Auswertung
l2, a21, g21, a22, g22 = np.genfromtxt('data/dotiert1.txt', unpack=True)
# Daten von Grad+Winkelminuten in Radiant umrechnen
d3 = (a21 + g21/60)*(np.pi)/180
d4 = (a22 + g22/60)*(np.pi)/180

# Differenz berechnen
ld2 = np.abs(d3-d4)

# Normieren
d2 = 5.1*10**(-3)
ld2_n = ld2/d2

# als txt speichern
np.savetxt('data/winkeldiff2.txt', ld2_n)

# dotiert2 Auswertung
l3, a31, g31, a32, g32 = np.genfromtxt('data/dotiert2.txt', unpack=True)
# Daten von Grad+Winkelminuten in Radiant umrechnen
d5 = (a31 + g31/60)*(np.pi)/180
d6 = (a32 + g32/60)*(np.pi)/180

# Differenz berechnen
ld3 = np.abs(d5-d6)
# Normieren
d3 = 5.1*10**(-3)
ld3_n = ld3/d3

# als txt speichern
np.savetxt('data/winkeldiff3.txt', ld3_n)

# Plotte theta/d gegen lambda^2
plt.plot(l1**2, ld1_n, 'x', label='GaAs undotiert')
plt.plot(l2**2, ld2_n, 'x', label='GaAs n-dotiert 1')
plt.plot(l3**2, ld3_n, 'x', label='GaAs n-dotiert 2')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.xlabel(r'$\lambda^2 \:/\:\mathrm{µm}^2$')
plt.ylabel(r'$\frac{\Theta}{d} \:/\:$rad$\mathrm{m}^{-1}}$')
plt.grid()
plt.legend()
plt.savefig('build/plot2.pdf')
plt.close()