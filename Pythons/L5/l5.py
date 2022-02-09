from pprint import pprint
def inp_list():
    n = input('Введіть кількість елементів массиву: ')
    z = []
    for i in range(int(n)):
        z.append(int(input(": ")))
    return z


def inp_matr():
    n, m = int(input('n: ')), int(input('m: '))
    matr = []
    for i in range(n):
        row = []
        for i in range(m):
            row.append(int(input(': ')))
        matr.append(row)
    print(matr)
    return matr


def func1():
    x = inp_list()
    z = list(filter(lambda y: y <= 0, x[2::2]))
    print(sum(z)/len(z), z)


def func2():
    k = 0
    x = inp_list()
    print(x)
    for i in x:
        if i >= 0:
            k+=1
    n = len(x)-k
    if (k-n)<0:
        x+=[i+1 for i in range(abs(k-n))]
        k += 1
    elif (k-n)>0:
        x+=[-(i+1) for i in range(abs(k-n))]
        n += 1
    else:
        return x
    return x


def func3():
    x = inp_matr()
    for i in range(len(x)):
        m = max(x[i])
        print(f'максимальний елемент {i} рядка: {m}')
        for j in range(len(x)):
            x[i][j] /= m
            x[i][j] = round(x[i][j],2)
    return x


def func4(i):
    x = inp_matr()
    x.pop(i)
    return x


def func5():
    inp = None
    exp = None
    while inp != 'Done':
        try:
            inp = input()
            exp = eval(inp)
            print(type(exp))
        except:
            "there is no such type"



#
print("Завдання1")
func1()
print("\nЗавдання2")
print(func2())
print("\nЗавдання3")
for i in func3():
    print(i)
print("\nЗавдання4")
print(func4(1))
print("\nЗавдання5")
func5()
