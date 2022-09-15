
from re import T
import matplotlib.pyplot as plt

data = [(0.3, 0.7, 1), (-0.6, 0.3, 0), (-0.1, -0.8, 0), (0.1, -0.45, 1)]
#w1 = 0.8
#w2 = -0.5
#n = 0.5

class Perceptrom:
    def __init__(self, w1, w2, n):
        self.w1 = w1
        self.w2 = w2
        self.n = n

    def calc(self, x1, x2):
        o = (x1 * self.w1) + (x2 * self.w2)

        if(o >= 0):
            return 1

        return 0

    def erro(self, t, y):
        return t - y

    def atualizar(self, peso, e, x):
        return peso + self.n * e * x


p = Perceptrom(0.95, -0.15, 0.5)

for d in data:
    o = p.calc(d[0], d[1])
    e = p.erro(d[2], o)
    color = "red"
    if(d[2] == 1):
        color = "blue"
    plt.scatter(d[0], d[1], c=color)

plt.plot([p.w1, p.w2], [p.w2, p.w1])

plt.show()


