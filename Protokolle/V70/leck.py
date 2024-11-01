import numpy as np
import matplotlib.pyplot as plt

# Turbomolekular
print('Turbomolekular:')

print('1:')
t, p = np.genfromtxt('content/data/turbomolekular/leckrate1.txt', unpack=True)
perr = np.genfromtxt('content/data/turbomolekular/plerr.txt', unpack=True)

# Fit
params, covariance_matrix = np.polyfit(t, p*10**(3), deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')

# Plot
plt.errorbar(t, p*10**(3), yerr=perr*10**(3), fmt='.k', label='Messwerte', capsize=1)
plt.plot(
    t,
    params[0] * t + params[1],
    label='Lineare Regression',
    linewidth=3,
)
plt.xlabel(r'$t/s$')
plt.ylabel(r'$p/ mbar\cdot 10^{-3}}$')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/turboleck1.pdf')
plt.close()

print('2:')
t, p = np.genfromtxt('content/data/turbomolekular/leckrate2.txt', unpack=True)
perr = np.genfromtxt('content/data/turbomolekular/leckrate2err.txt', unpack=True)

# Fit
params, covariance_matrix = np.polyfit(t, p*10**3, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')

# Plot
plt.errorbar(t, p*10**3, yerr=perr*10**3, fmt='.k', label='Messwerte', capsize=1)
plt.plot(
    t,
    params[0] * t + params[1],
    label='Lineare Regression',
    linewidth=3,
)
plt.xlabel(r'$t/s$')
plt.ylabel(r'$p/ mbar\cdot 10^{-3}}$')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/turboleck2.pdf')
plt.close()

print('3:')
t, p = np.genfromtxt('content/data/turbomolekular/leckrate3.txt', unpack=True)
perr = np.genfromtxt('content/data/turbomolekular/leckrate3err.txt', unpack=True)

# Fit
params, covariance_matrix = np.polyfit(t, p*10**(3), deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')

# Plot
plt.errorbar(t, p*10**(3), yerr=perr*10**(3), fmt='.k', label='Messwerte', capsize=1)
plt.plot(
    t,
    params[0] * t + params[1],
    label='Lineare Regression',
    linewidth=3,
)
plt.xlabel(r'$t/s$')
plt.ylabel(r'$p/ mbar\cdot 10^{-3}}$')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/turboleck3.pdf')
plt.close()

print('4:')
p, t = np.genfromtxt('content/data/turbomolekular/leckrate4.txt', unpack=True)
perr = np.genfromtxt('content/data/turbomolekular/leckrate4err.txt', unpack=True)

# Fit
params, covariance_matrix = np.polyfit(t, p*10**(3), deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')

# Plot
plt.errorbar(t, p*10**(3), yerr=perr*10**(3), fmt='.k', label='Messwerte', capsize=1)
plt.plot(
    t,
    params[0] * t + params[1],
    label='Lineare Regression',
    linewidth=3,
)
plt.xlabel(r'$t/s$')
plt.ylabel(r'$p/ mbar\cdot 10^{-3}}$')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/turboleck4.pdf')
plt.close()

# Drehschieber
print('Drehschieber:')
t, p1, p2, p3, p4, p5, p6 = np.genfromtxt('content/data/drehschieber/leckrate.txt', unpack=True)
p1err, p2err, p3err, p4err, p5err, p6err = np.genfromtxt('content/data/drehschieber/pleckerr.txt', unpack=True)
pm, pmerr = np.genfromtxt('content/data/drehschieber/pm.txt', unpack=True)

# p1
# Fit
params, covariance_matrix = np.polyfit(t, p1, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))
print('p1:')
for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')

# Plot
plt.errorbar(t, p1, yerr=p1err, fmt='.k', label='Messwerte', capsize=1)
plt.plot(
    t,
    params[0] * t + params[1],
    label='Lineare Regression',
    linewidth=3,
)
plt.xlabel(r'$t/s$')
plt.ylabel(r'$p_{1}/ mbar$')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/p1.pdf')
plt.close()

#p2
# Fit
params, covariance_matrix = np.polyfit(t, p2, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))
print('p2:')
for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')

# Plot
plt.errorbar(t, p2, yerr=p2err, fmt='.k', label='Messwerte', capsize=1)
plt.plot(
    t,
    params[0] * t + params[1],
    label='Lineare Regression',
    linewidth=3,
)
plt.xlabel(r'$t/s$')
plt.ylabel(r'$p_{2}/ mbar$')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/p2.pdf')
plt.close()

#p3
# Fit
params, covariance_matrix = np.polyfit(t, p3, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))
print('p3:')
for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')

# Plot
plt.errorbar(t, p3, yerr=p3err, fmt='.k', label='Messwerte', capsize=1)
plt.plot(
    t,
    params[0] * t + params[1],
    label='Lineare Regression',
    linewidth=3,
)
plt.xlabel(r'$t/s$')
plt.ylabel(r'$p_{4}/ mbar$')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/p3.pdf')
plt.close()

#p4
# Fit
params, covariance_matrix = np.polyfit(t, p4, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))
print('p4:')
for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')

# Plot
plt.errorbar(t, p4, yerr=p4err, fmt='.k', label='Messwerte', capsize=1)
plt.plot(
    t,
    params[0] * t + params[1],
    label='Lineare Regression',
    linewidth=3,
)
plt.xlabel(r'$t/s$')
plt.ylabel(r'$p_{4}/ mbar$')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/p4.pdf')
plt.close()

#p5
# Fit
params, covariance_matrix = np.polyfit(t, p5, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))
print('p5:')
for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')

# Plot
plt.errorbar(t, p5, yerr=p5err, fmt='.k', label='Messwerte', capsize=1)
plt.plot(
    t,
    params[0] * t + params[1],
    label='Lineare Regression',
    linewidth=3,
)
plt.xlabel(r'$t/s$')
plt.ylabel(r'$p_{5}/ mbar$')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/p5.pdf')
plt.close()

#p6
# Fit
params, covariance_matrix = np.polyfit(t, p6, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))
print('p6:')
for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')

# Plot
plt.errorbar(t, p6, yerr=p6err, fmt='.k', label='Messwerte', capsize=1)
plt.plot(
    t,
    params[0] * t + params[1],
    label='Lineare Regression',
    linewidth=3,
)
plt.xlabel(r'$t/s$')
plt.ylabel(r'$p_{6}/ mbar$')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/p6.pdf')
plt.close()

# pm
# Fit
params, covariance_matrix = np.polyfit(t, pm, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))
print('pm:')
for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')

# Plot
plt.errorbar(t, pm, yerr=pmerr, fmt='.k', label='Messwerte', capsize=1)
plt.plot(
    t,
    params[0] * t + params[1],
    label='Lineare Regression',
    linewidth=3,
)
plt.xlabel(r'$t/s$')
plt.ylabel(r'$p_{1}/ mbar$')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/pm.pdf')
plt.close()