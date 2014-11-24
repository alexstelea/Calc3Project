__author__ = 'alexstelea'

import math

import numpy as np
from numpy.linalg import qr


def givens_rotation(a, b):
    print a, b
    if b is 0:
        c = 1
        s = 0
    else:
        r = math.sqrt(a ** 2 + b ** 2)
        c = a / r
        s = -b / r
    return c, s


def qr_fact_givens(matrixA):
    m, n = matrixA.shape
    Q = [[float(x == y) for x in range(m)] for y in range(n)]
    print Q
    R = matrixA
    for j in range(n):
        for i in range(j, m - 1):
            G = np.eye(m)
            c, s = givens_rotation(R[i, i], R[i + 1, i])
            G[i, i] = c
            G[i + 1, i + 1] = c
            G[i, i + 1] = -s
            G[i + 1, i] = s

            R = np.dot(G, R)
            Q = np.dot(Q, G.T)
    return Q, R


if __name__ == '__main__':
    np.set_printoptions(suppress=True)
    a = np.array([[6., 5., 0.], [5., 1., 4.], [0., 4., 3.]])
    b = np.array([[12., -51., 4.], [6., 167., -68.], [-4., 24., -41.]])
    c = np.array([
        [-1., 0., -1.],
        [-1.23367806, 0.25907239, -1.],
        [-0.71892373, -0.23724483, -1.],
        [-1.87761058, 1.18289466, -1.],
        [-0.85812972, -0.13129385, -1.],
        [-1.42048733, 0.49859105, -1.],
        [-0.38289289, -0.36757717, -1.]])
    q, r = qr_fact_givens(a)
    e, f = qr(a)
    print np.dot(q, r)
    print np.dot(e, f)
    print a
    print q
    print e
    print r
    print f

