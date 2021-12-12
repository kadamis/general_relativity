import math
import matplotlib.pyplot as plt
import scipy.constants as sc

sc.c = 100

x = []
y = []
z = []
w = []


for i in range(sc.c):

    x.append(i)

    g = 1/(math.sqrt(1-i**2/sc.c**2))

    y.append(g)

    print(x,y)

    
    for j in range(10):

        z.append(j)
        
        T_tonos = j*g

        w.append(T_tonos)

        print (z, w)
    
plt.plot(z,w)
plt.show()

plt.plot(x,y)
plt.show()
