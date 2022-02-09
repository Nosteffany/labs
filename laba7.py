import math as m
import laba5


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

def chance(lamb, k):
    return (lamb ** k / m.factorial(k)) * m.exp(- lamb)


def first():
    amount_of_cases = 1000

    lamd = 4
    amount_of_experiments = 20

    count = [0 for i in range(amount_of_experiments)]
    exponenta = m.exp(-lamd)

    for i in range(amount_of_experiments):

        r = laba5.Rivn(amount_of_cases, 0, 1)[1]
        first_cond = 0
        second_cond = 0
        for j in range(amount_of_cases):
            first_cond += lamd**j / m.factorial(j)
            second_cond += first_cond + lamd**j / m.factorial(j)


            if exponenta*first_cond <= r[j] <exponenta*second_cond:
                count[i] += 1
    return count

def second():
    amount = 20
    lamb = 4


    for j in range(0, amount):
        p = 0.002
        n = int(lamb / p)
        print("amout of attempts = ", toFixed(n, 0),
              "\nlambda = ", lamb,
              "\nchance to be lucky = ", p)

        r = laba5.Rivn(n, 0, 1)[1]
        k = 0
        for i in range(0,n):
            if r[i] <= p:
                k += 1
        print("amount of successful attempts = ", k)
        print(j,"chance to be lucky :", [toFixed(r, 5) for r in r])
        print("\n\n-------------------------------------------------------")


print(first())
# second()
