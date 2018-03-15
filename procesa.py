import numpy as np

datos=np.loadtxt('monthrg.dat')
tiempo=datos[:,0]+((datos[:,1]-1)/12.0)
manchas= datos[:,3]

ii = tiempo>1900
tiempo=tiempo[ii]
manchas=manchas[ii]

salida = np.array([tiempo,manchas])


np.savetxt('fecha_manchas.dat', salida.T)




