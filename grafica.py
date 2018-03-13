import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,100,500)
y=np.exp(x/(-50))*np.sin(x)

plt.figure()
plt.plot(x,y)
plt.savefig('grafica.png')



