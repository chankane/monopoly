import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1)
f = lambda x: np.sqrt(1 - (1 - x)**2)
y = f(x)

plt.plot(x, y)

#plt.show()

#xx = np.linspace((0, 0), (1, 1), 10)
#print(xx)

def __harf_slerp(pos0, pos1, rate):
    l = 0


def interpolation(val0, val1, rate):
    x = np.linspace(val0, val1, 100)