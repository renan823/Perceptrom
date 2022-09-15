#histogramas
import numpy

import matplotlib.pyplot as plt


#distribuição de dados 'uniformes', usando o uniform
x = numpy.random.uniform(0.0, 5.0, 2500)

plt.hist(x, 100)
plt.show()

#distribuição de dados 'normais', usando o normal
x = numpy.random.normal(5.0, 1.0, 100000)
plt.hist(x, 100)
plt.show()

'''
o histograma 'normal' gera 100.000 valores, o valor médio é 5 e
o desvio padrão é 1
Os valores se concentram perto de 5


numpy.random.normal(valor médio, desvio padrão, qnt de números gerados)
'''
