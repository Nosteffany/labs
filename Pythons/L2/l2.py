from math import pi, sqrt


def ring_square(r1, r2):
    return abs(pi*r1**2 - pi*r2**2)


def calc(x):
    if x >= pi and x < 8.5:
        return x-1
    elif x > 8.5 and x < pi:
        return sqrt(abs(pi-x))
    elif abs(x) >= 8.5:
        return 2.7



def func1(N, M, x, y):
    return min(N-x, x, M-y, y)


r1 = int(input("радіус першого круга: "))
r2 = int(input("радіус другого круга: "))
print("Площа кільця = ",round(ring_square(r1,r2),3))
print("Завдання2\n",func1(100,50,50,30))
print("Завдання3\n",calc(10))
