import numpy as np
import matplotlib.pyplot as plt

datos=np.loadtxt('fecha_manchas.dat')
x=datos[:,0]
y=datos[:,1]
plt.figure()
plt.scatter(x,y,s=0.3)
plt.savefig('grafica.pdf')
