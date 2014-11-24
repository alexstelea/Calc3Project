__author__ = 'alexstelea'

import math

import numpy as np
from numpy.linalg import qr


def givens_rotation(a, b):
    # print a, b
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
    R = matrixA
    for i in range(n-1):
        for j in range(m-1):
            if i is j:
                pivot_loc = i
            if i < j:
                if R[j, i]:
                    G = np.eye(m)
                    # print (pivot_x, pivot_y)
                    c, s = givens_rotation(R[pivot_loc, pivot_loc], R[pivot_loc, pivot_loc+1])
                    print c,s
                    G[pivot_loc, pivot_loc] = c
                    G[pivot_loc, pivot_loc+1] = -s
                    G[pivot_loc+1, pivot_loc] = s
                    G[pivot_loc+1, pivot_loc+1] = c
                    print G
                    R = np.dot(G.T, R)
                    Q = np.dot(Q, G)
    print
    print Q
    print R
    print
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
    q, r = qr_fact_givens(c)
    e, f = qr(c)
    print e
    print f
    print
    print
    # print q
    # print e
    # print r
    # print f
    #
