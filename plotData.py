import matplotlib.pyplot as plt
import numpy as np

with open('data','r') as f:
  lines = f.readlines()

lines = [line.strip().split() for line in lines]

Tskin=[float(item[0]) for item in lines]
dt=600
time=np.arange(0,(len(Tskin))*dt,dt)


#x=np.arange(0,2*(np.pi),0.1)
#y=np.sin(x)

plt.plot(time,Tskin)

plt.show()
