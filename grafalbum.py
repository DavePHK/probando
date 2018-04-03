import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt('datos.txt')
n= len(datos[:,0])
t=np.linspace(0,n,n)
plt.figure()
plt.scatter(t,datos[:,0], label='n_en_album')
plt.scatter(t,datos[:,1], label='n_repetidas',c='r')
plt.legend()
plt.savefig('grafalbum.pdf')
