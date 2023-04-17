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
d1 = a11 + g11/60
d2 = a12 + g12/60