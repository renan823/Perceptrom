#dispersão

import matplotlib.pyplot as plt
import numpy



velocidades = [10, 20, 15, 45, 12]
idade = [60, 45, 53, 34, 6]

plt.scatter(velocidades, idade)
plt.show()

'''

velocidades = numpy.random.normal(5.0, 1.0, 1000)
idade = numpy.random.normal(10.0, 2.0, 1000)

plt.scatter(velocidades, idade)
plt.show()
'''
'''
dispersa os valores em eixos x e y através de 'bolinhas'
'''

