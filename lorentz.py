import math
import matplotlib.pyplot as plt
import scipy.constants as sc

sc.c = 100

x = []
y = []
z = []

for i in range(sc.c):

    x.append(i)

    g = 1/(math.sqrt(1-i**2/sc.c**2))

    y.append(g)

    print(x,y)

    v_rel = i/(g**2)

    z.append(v_rel)

    print(x,v_rel)
    
#Plot of relative speed.    
plt.plot(x,z)
plt.show()

#Plot of Lorentz's factor.
plt.plot(x,y)
plt.show()
