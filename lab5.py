import rel_matrix as rlm
from pprint import pprint


xx = [[1,1,0,1,0],
    [1,1,1,1,1],
    [1,0,0,1,1],
    [1,1,1,1,1],
    [0,1,0,1,0]]
yy = [[1,1,0,1,0],
    [1,1,1,1,1],
    [1,0,0,1,1],
    [1,1,1,1,1],
    [0,1,0,1,0]]
def eq(m):
    result = rlm.cross_r(m,rlm.rev_r(m))
    return result


def s_per(m):
    result = rlm.diff_r(m,rlm.rev_r(m))
    return result


def tolerance(m):
    omega = [[1]*len(m) for i in range(len(m))]
    return rlm.union_r(rlm.diff_r(omega,rlm.union_r(m,rlm.rev_r(m))), (rlm.cross_r(m,rlm.rev_r(m))))


def prop(m):
    maxx = None
    minor = None
    minn = None
    major = None
    for i in range(len(m)):
        maxx = True
        minor = True
        minn = True
        major = True
        for j in range(len(m)):
            if m[i][j] == 0:
                maxx = False
            if m[i][j] == 1:
                minor = False
            if m[j][i] == 0:
                minn = False
            if m[j][i] == 1:
                major = False
        if maxx:
            print(f'x{i} - максимум')
        if minn:
            print(f'x{i} - мінімум')
        if major:
            print(f'x{i} - мажоранта')
        if minor:
            print(f'x{i} - міноранта')
prop(xx)
print("\nСтрогої переваги")
pprint(s_per(yy))
print("\nЕквівалентності")
pprint(eq(xx))
print("\nТолерантності")
pprint(tolerance(xx))


# z = [[1,1,0,1],
#     [0,1,0,1],
#     [0,1,1,0],
#     [1,0,1,1]]
# c = [[1,1,0,1],
#     [0,1,0,1],
#     [0,1,1,0],
#     [1,0,1,1]]
