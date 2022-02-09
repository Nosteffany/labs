from math import log


def func1():
    def calc(x):
        return (1.5*x-log(2*x))/(3*x+1)
    k = 6
    x = None
    while True:
        try:
            x = float(input("Start point: "))
        except ValueError:
            print('Only numbers can be used')
            continue
        break
    while k>0:
        if x >= 2.5 and x <= 9:
            print(f'Значення в точці {x}', calc(x))
            x+=0.8
            k-=1
        elif x >= 0.8:
            print(f'Значення в точці {x}', calc(x))
            x+=1.2
            k-=1


def func2(a,b):
    if a == b:
        print(a)
    else:
        for i in range(a,b+1):
            print(i)



func1()
print('\nЗавдання2')
func2(1,10)
