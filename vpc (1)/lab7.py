x = [1,2,3]


def func(a = []):
    a.append(1)
    return a



for i in range(4):
    print(func())
