import matplotlib.pyplot as plt

alpha = 1
beta = 1.7
c = 0.01
b = 0.01
n = 60
tau = 0.1
n0 = 50
m0 = 83

def func(alpha,beta,c,b,nn,tau,n0,m0):
    m = [m0]
    n = [n0]
    for i in range(1,nn):
        n.append(int(n[i-1]/(1-tau*(alpha-c*m[i-1]))))
        m.append(int(m[i-1]/(1-tau*(-beta+b*n[i-1]))))
    # k = 0
    for i in range(nn):
        print(f"Жертви: {n[i]}| Хижаки: {m[i]}")
    return n,m
a = func(alpha,beta,c,b,n,tau,n0,m0)

# print(a)


k = list(range(len(a[0])))

plt.plot(k,a[0],'b')
plt.plot(k,a[1],'r')


plt.show()
