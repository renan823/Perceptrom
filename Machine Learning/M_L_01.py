#machine L - 1 : média, moda e mediana


import numpy

precos = [86,87,88,86,87,85,86]
#[86,87,88,86,87,85,86]
#[99,86,87,88,111,86,103,87,94,78,77,85,86]
#----------------------
#media

media = numpy.mean(precos)

print(media)

#-----------------
#mediana

mediana = numpy.median(precos)
print(mediana)

#----------

'''moda = stats.mode(precos)
print(moda)'''

#-----------

desvio = numpy.std(precos)
print(desvio)
