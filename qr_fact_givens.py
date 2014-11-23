__author__ = 'alexstelea'


from math import *
import numpy as np

def copysign(a, b):
    if (b < 0 and a > 0) or (b > 0 and a < 0):
        a = -a
    return a

def csr(a, b):
    if (b == 0):
        c = copysign(1, a)
        s = 0
        r = abs(a)
    elif (a == 0):
        c = 0
        s = copysign(1, b)
        r = abs(b)
    elif (abs(b) > abs(a)):
        t = a/b
        u = copysign(sqrt(1+t*t), a)
        s = 1.0/u
        c = s*t
        r = b*u
    else:
        t = b/a
        u = copysign(sqrt(1+t*t), a)
        c = 1.0/u
        s = c*t
        r = a*u

    return (c, s, r)


def qr_fact_givens(matrixA):
    matrixA = np.matrix(matrixA)
    m, n = matrixA.shape
    if m != n:
        raise ValueError, "Matrix A must be a square"
    else:
        P = [[float(x == y) for x in range(m)] for y in range(n)]
        for i in range(0, m-1):
            for j in range(i+1, m):
                a, b = matrixA[i][i], matrixA[j][i]
                if abs(b) > (1.0e-8):
                    c, s, r = csr(a, b)
                    Pij = [[float(x == y) for x in range(m)] for y in range(m)]
                    Pij[i][i] = c
                    Pij[i][j] = s
                    Pij[j][i] = -s
                    Pij[j][j] = c
                    print "Rotation Matrix for i, j, r =", i, j, r
                    # matprint(Pij)
    return P, matrixA



if __name__ == '__main__':qr_fact_givens(([[12, -51, 4], [6, 167, -68], [-4, 24, -41]]))