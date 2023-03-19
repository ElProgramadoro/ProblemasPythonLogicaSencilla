#este programa calcula el area de un circulo
import numpy as np
p = np.pi
def calculo(r):
    a = p*(r**2)
    return print('Area = ', round(a,3))

r = int(input('Inserte el radio del ciculo: '))
calculo(r)