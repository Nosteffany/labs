from rel_matrix import rev_r, cross_r, compose_r, compl_r


matrix = [[0,1,1,1,0],[0,1,0,1,0],[0,0,0,0,0],[0,0,1,1,1],[0,1,0,0,0]]
# y = [[1,0,0],[0,0,1],[1,0,1]]
# z = [[0,1,1],[0,1,1],[0,0,0]]

def refleksy(m):
    for i in range(len(m)):
        if m[i][i] != 1:
            return False
    return True


def a_refleksy(m):
    for i in range(len(m)):
        if m[i][i] != 0:
            return False
    return True


def symetry(m):
    return m == rev_r(m)


def a_symetry(m):
    return(a_refleksy(m))


def ant_symetry(m):
     res = cross_r(m,rev_r(m))
     for i in range(len(m)):
         for j in range((len(m))):
             if i != j:
                 if res[i][j] != 0:
                     return False
     return True


def transitivity(m):
    return compose_r(m,m)==m


def n_transitivity(m):
    return compose_r(compl_r(m),compl_r(m))==compl_r(m)


def super_transitivity(m):
    return transitivity(m) and n_transitivity(m)


for i in matrix:
    print(i)

print("\nрефлективність: ",refleksy(matrix))
print("антирефлексивність: ",a_refleksy(matrix))
print("симетричність: ", symetry(matrix))
print("асиметричність: ",a_symetry(matrix))
print("антисиметричність: ",ant_symetry(matrix))
print("транзитивність: ",transitivity(matrix))
print("негативна транзитивність: ",n_transitivity(matrix))
print("сильна транзитивність: ",super_transitivity(matrix))
