import threading
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

def move(pos0, pos1, time):
    anim_thread = threading.Thread(target=func1)


def s


def __interpolation(val0, val1, rate):
    return rate * (val1 - val0) + val0

class MockPlayer:
    def __init__(self):
        self.__pos = [0, 0]

    def move(self, count):