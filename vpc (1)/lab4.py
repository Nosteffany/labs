from random import random
import matplotlib.pyplot as plt

def monte_carlo(n):
    k = 0
    xx = []
    yy = []
    for i in range(n):
        x = -2 + 4*random()
        y = -2 + 4*random()
        if (-x**3+y**4<3) and (x-y<1):
            k+=1
            xx.append(x)
            yy.append(y)
    mk = 16*k/n
    return {'x':xx,'y':yy,'square':mk}


result = monte_carlo(2000000)
print(result.get('square'))
plt.scatter(result.get('x'),result.get('y'))
plt.show()
