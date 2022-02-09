from lab6 import a
import matplotlib.pyplot as plt

k = list(range(len(a[0])))

plt.plot(k,a[0],'b')
plt.plot(k,a[1],'r')


plt.show()
# print(a)
