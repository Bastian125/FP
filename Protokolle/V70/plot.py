import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat

#t, p1, p2, p3, p4, p5, p6 = np.genfromtxt('content/data/drehschieber/leckrate.txt', unpack=True)
#p1err, p2err, p3err, p4err, p5err, p6err = np.genfromtxt('content/data/drehschieber/pleckerr.txt', unpack=True)
#
#p1u = unp.uarray(p1, p1err)
#p2u = unp.uarray(p2, p2err)
#p3u = unp.uarray(p3, p3err)
#pm = (p1u+ p2u+ p3u)/3
#p = np.column_stack((np.round(unp.nominal_values(pm), decimals=1), np.round(unp.std_devs(pm), decimals=1)))
#np.savetxt('content/data/drehschieber/pm.txt', p)

#t, p = np.genfromtxt('content/data/drehschieber/evakuierung.txt', unpack=True)
#perr = 0.1*p
#
#np.savetxt('content/data/drehschieber/pevakerr.txt', perr)

#V = ufloat(33, 0.1)
#p = ufloat(6, 1.8)
#m = ufloat(5.3, 0.01)
#S = (V*m)/p
#print(S)

#V = ufloat(34, 0.1)
#m = ufloat(-0.011, 0.001)
#S=-m*V
#print(S)

#t, p2 = np.genfromtxt('content/data/turbomolekular/leckrate2.txt', unpack=True)
#p3, t = np.genfromtxt('content/data/turbomolekular/leckrate3.txt', unpack=True)
#p4, t = np.genfromtxt('content/data/turbomolekular/leckrate4.txt', unpack=True)
#
#p2err = 0.3*p2
#p3err = 0.3*p3
#p4err = 0.3*p4
#
#np.savetxt('content/data/turbomolekular/leckrate2err.txt', p2err)
#np.savetxt('content/data/turbomolekular/leckrate3err.txt', p3err)
#np.savetxt('content/data/turbomolekular/leckrate4err.txt', p4err)