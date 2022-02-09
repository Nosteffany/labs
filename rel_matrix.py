from pprint import pprint


# x = [[0,1,1,1,0],[0,1,0,1,0],[0,0,0,0,0],[0,0,1,1,1],[0,1,0,0,0]]
c = [[1,1,0,0],[0,1,1,0],[1,0,1,1],[1,1,1,0]]
z = [[0,1,1,1],[1,1,1,0],[0,1,1,1],[0,1,1,0]]

x = [[1,1,1,1],[0,1,1,1],[0,1,0,0],[1,0,1,0]]
y = [[0,1,0,1],[0,0,0,1],[0,1,0,0],[0,0,1,0]]
# y = [[0,0,1,0,1],[1,0,0,0,1],[0,1,1,0,0],[0,1,0,0,0],[1,0,1,1,1]]


def incl_r(m1,m2):
    for i in range(len(m2)):
        for j in range(len(m2)):
            if m2[i][j] < m1[i][j]:
                return False
    return True
# print(incl_r(c,z))

#Рівність
def equal_r(m1,m2):
    return m1 == m2


def union_r(m1,m2):
    # result = m1[:]
    result = [[1]*len(m1) for i in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1)):
            if m1[i][j] or m2[i][j] == 1:
                result[i][j] = 1
            else:
                result[i][j] = 0
    return result

#
def cross_r(m1,m2):
    # result = m1[:]
    result = [[1]*len(m1) for i in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1)):
            if m1[i][j] == m2[i][j] == 1:
                result[i][j] = 1
            else:
                result[i][j] = 0
    return result

#
def diff_r(m1,m2):
    result = m1[:]
    # result = [[1]*len(m1) for i in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1)):
            if m1[i][j] == 1 and m2[i][j] == 1:
                result[i][j] = 0
    return result

#
def sym_diff_r(m1,m2):
    # result = m1[:]
    result = [[1]*len(m1) for i in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1)):
            if m1[i][j] == m2[i][j] == 1:
                result[i][j] = 0
            elif m1[i][j] != m2[i][j]:
                result[i][j] = 1
            else:
                result[i][j] = 0
    return result

#
def compl_r(m):
    # result = m[:]
    result = [[1]*len(m) for i in range(len(m))]
    for i in range(len(m)):
        for j in range(len(m)):
            # m[i][j] = abs(m[i][j]-1)
            result[i][j] = abs(m[i][j]-1)
    return result


def rev_r(m):
    # result = m[:]
    result = [[0 for i in range(len(m))]for j in range(len(m))]
    for i in range(len(m)):
        for j in range(len(m)):
            result[j][i] = m[i][j]
    return result


def d_rev_r(m):
    return compl_r(rev_r(m))
# print(d_rev_r(x1))

def compose_r(m1, m2):
    result = [[0 for i in range(len(m1))]for j in range(len(m1))]
    m2 = rev_r(m2)
    n = len(m1)
    buff = []
    z = []
    for i in range(n):
        for j in range(n):
            z.append(list(zip(m1[i],m2[j])))
    for i in z:
        buff.append((max([min(j)for j in i])))
    return [buff[i*n:i*n+n] for i in range(n)]

i = [0,2]
xx = [[1,0,1],[1,1,0],[0,0,1]]

def constr_r(x,ind):
    res = []
    n = len(ind)
    for i in range(len(x)):
        for j in range(len(x)):
            if i in ind and j in ind:
                res.append(x[i][j])
    return [res[i*n:i*n+n] for i in range(n)]


if __name__ == '__main__':
    pass
    print("Композиція\n")
    pprint(compose_r(x,y))
    print("Обернене двоїсте\n")
    pprint(d_rev_r(x))
    print("Обернене\n")
    pprint(rev_r(x))
    print("Доповнення\n")
    pprint(compl_r(x))
    print("Різниця симетр\n")
    pprint(sym_diff_r(x,y))
    print("Перетин\n")
    pprint(cross_r(x,y))
    print("Об*єднання\n")
    pprint(union_r(x,y))
    print("Рівність\n")
    pprint(equal_r(x,y))
    print("Звуження\n")
    pprint(constr_r(xx,i))
    print("Різниця\n")
    pprint(diff_r(x,y))

# print(equal_r(x,y))
