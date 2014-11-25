__author__ = 'alexstelea'

import math
import numpy as np

#used for testing qr
from numpy.linalg import qr


def givens_rotation(R, a, b):
    i, j = a
    m, n = b
    val_a = R[i][j]
    val_b = R[m][n]

    if b is 0:
        c = 1
        s = 0
    else:
        r = math.sqrt(val_a**2 + val_b**2)
        c = val_a / r
        s = val_b / r
    return c, s


def qr_fact_givens(matrixA):
    m, n = matrixA.shape
    Q = np.eye(m)
    R = matrixA
    for i in range(n):
        for j in range(m):
            if i is j:
                pivot_xy = (j, i)
            if i < j and R[j, i]:
                G = np.eye(m)
                c,s = givens_rotation(R, pivot_xy, (j, i))
                G[j][j] = c
                G[i][i] = c
                G[i][j] = s
                G[j][i] = -s

                R = np.dot(G, R)
                Q = Q.dot(G.T)
    return Q, R


if __name__ == '__main__':
    np.set_printoptions(suppress=True)
    print "Uncomment the test cases below :)"
    # a = np.array([[6., 5., 0.], [5., 1., 4.], [0., 4., 3.]])
    # b = np.array([[12., -51., 4.], [6., 167., -68.], [-4., 24., -41.]])
    # c = np.array([
    #     [-1., 0., -1.],
    #     [-1.23367806, 0.25907239, -1.],
    #     [-0.71892373, -0.23724483, -1.],
    #     [-1.87761058, 1.18289466, -1.],
    #     [-0.85812972, -0.13129385, -1.],
    #     [-1.42048733, 0.49859105, -1.],
    #     [-0.38289289, -0.36757717, -1.]])
    # q, r = qr_fact_givens(a)
    # print np.dot(q,r)
