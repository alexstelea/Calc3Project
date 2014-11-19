__author__ = 'alexstelea'



from math import sqrt
from pprint import pprint



def Q_i(Q_min, i, j, k):
    if i<k or j<k:
        return float(i==j)
    else:
        return Q_min[i-k][j-k]

def norm(x):
    return sqrt(sum([x[i]**2 for i in range(len(x)) ]))

def mult_matrix(M, N):
    tuple_N = zip(*N)
    return[[sum(el_m * el_n for el_m, el_n in zip(row_m, col_n)) for col_n in tuple_N] for row_m in M]

def trans_matrix(M):
    n = len(M)
    return[[M[i][j] for i in range(n)] for j in range(n)]

def qr_fact_givens(matrixA):
    n = len(matrixA)
    R = matrixA
    Q = [[0.0] * n for i in range(n)]

    for k in range(n-1):
        identity_matrix = [[float(i == j) for i in range(n)]for j in range(n)]
        x = [row[k] for row in R[k:]]
        e = [row[k] for row in identity_matrix[k:]]
        alpha = -cmp(x[0],0) * norm(x)

        u = map(lambda p, q: p + alpha * q, x, e)
        norm_u = norm(u)

        v = map(lambda p: p/norm_u,u)

        Q_min = [[float(i==j) - 2.0 * v[i] * v[j] for i in xrange(n-k)]for j in xrange(n-k)]

        Q_t = [[Q_i(Q_min, i,j,k) for i in xrange(n)] for j in xrange(n)]

        if k == 0:
            Q = Q_t
            R = mult_matrix(Q_t, matrixA)
        else:
            Q = mult_matrix(Q_t, Q)
            R = mult_matrix(Q_t, R)


    print "A:"
    pprint(matrixA)

    print "Q:"
    pprint(Q)

    print "R:"
    pprint(R)




if __name__ == '__main__':qr_fact_givens(([[12, -51, 4], [6, 167, -68], [-4, 24, -41]]))
