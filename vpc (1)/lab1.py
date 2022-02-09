from random import randint,random
import statistics as sts

def lin_rand(seed):
    M = 2**31
    A = 16807
    C = 3928

    seed = (seed*A+C)%M
    return seed


def sq_rand(seed):
    M = 2**31
    A = 16807
    C = 3928
    D = 4
    return (D*seed**2 + A*seed + C)%M

# x = []
# y = []
# n = 50
#
# for i in range(n):
#     x.append(lin_rand(randint(1,10000000))%2)
#     y.append(sq_rand(randint(1,10000000))%2)
#
# aa = []
# for i in range(50):
#     aa.append(random())

# print(sts.variance(aa))
#
# print("лін. конгруентний метод")
# print('дисп',round(sts.pvariance(x),5))
# print('математичне очікування ',sum(x),'\n')
# print("квад. конгруентний метод")
# print('дисп',round(sts.pvariance(y),5))
# print('математичне очікування ',sum(y)/n)
