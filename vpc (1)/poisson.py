from math import factorial, exp
import random


def poisson_1(l):
    i = 1
    result = []
    while len(result) != 20:
        r = random.random()
        while len(result) != 20:
            if exp(-l) * sum((l**k) / factorial(k) for k in range(i-1)) <= r < exp(
                    -l) * sum((l**k) / factorial(k) for k in range(i)):
                result.append(i)
                r = random.random()
                i = 1
            else:
                i += 1
        break
    return result


def second_method(l,p=0.1):
    n = int(l/p)
    # n=l/p
    result = []
    for i in range(20):
        k = 0
        for j in range(n):
            if random.random() <= p:
                k += 1
        result.append(k)
    return result



f = poisson_1(4)
s = second_method(4)
print('Пуассон1', f)
print('Пуассон2', s)
