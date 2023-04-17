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

# undotiert Auswertung
l1, a11, g11, a12, g12 = np.genfromtxt('data/undotiert.txt', unpack=True)
# Daten von Grad+Winkelminuten in Radiant umrechnen
d1 = (a11 + g11/60)*(np.pi)/180
d2 = (a12 + g12/60)*(np.pi)/180

# Differenz berechnen
ld1 = np.abs(d1-d2)

# als txt speichern
np.savetxt('winkeldiff1.txt', ld1)