from random import random
from pprint import pprint

values = [1, 8, 3, 5, 11]
prob = [0.11, 0.25, 0.14, 0.2, 0.3]

#ГЕНЕРУВАННЯ ІНТЕРВАЛІВ
def gen_intervals(x):
    summ = 0
    res = []
    for i in prob:
        a = [summ]
        summ += i
        a.append(summ)
        res.append(a)
    return res

#фУНКЦІЯ НАЛЕЖНОСТІ ПРОМІЖКУ
def match(i, value):
    return value > i[0] and value <= i[1]

#ГЕНЕРУВАННЯ ПОСЛІДОВНОСТІ
def discrete_value(n, values, p):
    #
    int_p  = gen_intervals(p)
    result = []
    for i in range(n):
        # rn - ВИПАДКОВЕ ЗНАЧЕННЯ [0,1]
        rn = round(random(),2)
        for j in range(len(int_p)):
            if match(int_p[j],rn):
                result.append(values[j])
                continue

    return result


r = discrete_value(100,values,prob)
print(r)
for i in values:

    print(f"Кількість значень величини {i} = {r.count(i)}")










# gener(prob)
