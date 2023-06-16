import numpy as np
import matplotlib.pyplot as plt
from uncertainties import unumpy as unp

# Turbomolekular
print('Turbomolekular')

t, p1 = np.genfromtxt('content/data/turbomolekular/evakuierung1.txt', unpack=True)
t, p2 = np.genfromtxt('content/data/turbomolekular/evakuierung2.txt', unpack=True)
t, p3 = np.genfromtxt('content/data/turbomolekular/evakuierung3.txt', unpack=True)
p1err = np.genfromtxt('content/data/turbomolekular/p1err.txt', unpack=True)
p2err = np.genfromtxt('content/data/turbomolekular/p2err.txt', unpack=True)
p3err = np.genfromtxt('content/data/turbomolekular/p3err.txt', unpack=True)

p1 = unp.uarray(p1, p1err)
p2 = unp.uarray(p2, p2err)
p3 = unp.uarray(p3, p3err)

# Mittelwert bilden
p = (p1+p2+p3)/3

# p0 und pe sind die Start- und Endwerte
p0 = p[0]
pe = p[24]

# Endwert aus p entfernen
p = p[0:23]
t = t[0:23]
x = unp.log((p - pe)/(p0 - pe))

plt.errorbar(t, unp.nominal_values(x), yerr=unp.std_devs(x), fmt='o', label='Messwerte')
# Fit 1
print('Fit 1')
params, covariance_matrix = np.polyfit(t[0:4], unp.nominal_values(x[0:4]), deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')

plt.plot(
    t[0:4],
    params[0] * t[0:4] + params[1],
    label='Lineare Regression 1',
    linewidth=3,
)

# Fit 2
print('Fit 2')
params, covariance_matrix = np.polyfit(t[4:23], unp.nominal_values(x[4:23]), deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')

plt.plot(
    t[4:23],
    params[0] * t[4:23] + params[1],
    label='Lineare Regression 2',
    linewidth=3,
)

plt.xlabel(r'$t/s$')
plt.ylabel(r'$ln(\frac{p(t)-p_E}{p_0 - p_E})$')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/turboevak.pdf')
plt.close()

# Drehschieber
print('Drehschieber')
t, p = np.genfromtxt('content/data/drehschieber/evakuierung.txt', unpack=True)
perr = np.genfromtxt('content/data/drehschieber/pevakerr.txt', unpack=True)

p = unp.uarray(p, perr)

# p0 und pe sind die Start- und Endwerte
p0 = p[0]
pe = p[60]

# Endwert aus p entfernen
p = p[0:59]
t = t[0:59]
x = unp.log((p - pe)/(p0 - pe))

plt.errorbar(t, unp.nominal_values(x), yerr=unp.std_devs(x), fmt='o', label='Messwerte', markersize=3)

# Fit 1
print('Fit 1')
params, covariance_matrix = np.polyfit(t[0:22], unp.nominal_values(x[0:22]), deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error}')

plt.plot(
    t[0:22],
    params[0] * t[0:22] + params[1],
    label='Lineare Regression 1',
    linewidth=3,
)

# Fit 2
print('Fit 2')
params, covariance_matrix = np.polyfit(t[22:59], unp.nominal_values(x[22:59]), deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error}')

plt.plot(
    t[22:59],
    params[0] * t[22:59] + params[1],
    label='Lineare Regression 2',
    linewidth=3,
)

plt.xlabel(r'$t/s$')
plt.ylabel(r'$ln(\frac{p(t)-p_E}{p_0 - p_E})$')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/drehevak.pdf')
plt.close()