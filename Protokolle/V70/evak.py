import numpy as np
import matplotlib.pyplot as plt

# Turbomolekular
t, p1 = np.genfromtxt('content/data/turbomolekular/evakuierung1.txt', unpack=True)
t, p2 = np.genfromtxt('content/data/turbomolekular/evakuierung2.txt', unpack=True)
t, p3 = np.genfromtxt('content/data/turbomolekular/evakuierung3.txt', unpack=True)

# Drehschieber