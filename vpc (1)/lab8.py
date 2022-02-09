from random import choice,random
from scipy.stats import truncnorm
import matplotlib.pyplot as plt

def norm_d(m,sigm,n=1):
    x = [round(sum(random() for i in range(12)),2)for j in range(n)]
    y = [round(sigm*(i-6)+m,2) for i in x]
    return y



# print(norm_d(0,9,1))

def veiner(k,t):
    h = t/k
    w = 0
    k = 0
    result = []
    while k<=t:
        ww = []
        kk = []
        rn = norm_d(0,h**2)
        w += rn[0]
        result.append((w,k))
        k+=h
    return result

aaa = veiner(30,30)

for i in range(20):
    aaa = veiner(10,30)
    aa = [i[0] for i in aaa]
    bb = [i[1] for i in aaa]
    plt.plot(bb,aa,choice('rbgycm'))






plt.show()
