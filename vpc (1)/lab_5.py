from random import random, choice
from math import log
from pprint import pprint
import scipy.stats as ss



def exp_d(l, n):
    result = []
    for i in range(n):
        result.append(round((-1*log(random()))/l,4))
    return(result)


def r_d(a, b, n):
    result = []
    for i in range(n):
        x = (b-a)*random() + a
        result.append(round(x,4))
    return result

zz = [0.01*i for i in range(50)]


def norm_d(m,sigm,n):
    x = [sum(random() for i in range(12))for j in range(n)]
    y = [sigm*(i-6)+m for i in x]
    return y


def chi_test(arr):
    mark = False
    a,b = ss.normaltest(arr)
    if a<b:
        mark = True
    return f"емпірична {a},критична {b}, розподіл є нормальним {mark}"


z = norm_d(2,1,100)
# print(z)
print(chi_test(z))
# pprint(exp_d(6,100))
# pprint(r_d(-1,6,100))
