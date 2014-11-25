__author__ = 'alexstelea'

import numpy as np

# used for testing
from numpy.linalg import qr


from helpers import norm, embed_matrix


def householder_reflection(col):
    n_height = len(col)
    m_matrix = np.eye(n_height, 1)
    I = np.eye(n_height)
    v = np.array([x + y for x, y in zip(col, norm(col) * m_matrix)])
    u = v / norm(v)
    return I - 2 * u * u.T

def qr_fact_householder(matrixA):
    rows, cols = matrixA.shape
    first_col_H = matrixA.T[0]
    H = householder_reflection(first_col_H)
    Q = H

    for i in range(cols):
        resultant_matrix = np.dot(Q, matrixA).T
        col = resultant_matrix[i, i:]
        minor = householder_reflection(col)
        I = np.eye(rows)
        H = embed_matrix(I, minor)
        Q = np.dot(H, Q)

    R = np.dot(Q, matrixA)
    return Q.T, R

if __name__ == '__main__':
    np.set_printoptions(suppress=True)
    print "Uncomment the test cases below :)"
    # a = np.array([
    #     [4, 1, -2, 2],
    #     [1, 2, 0, 1],
    #     [-2, 0, 3, -2],
    #     [2, 1, -2, -1]
    # ])
    # c = np.array([
    #     [-1., 0., -1.],
    #     [-1.23367806, 0.25907239, -1.],
    #     [-0.71892373, -0.23724483, -1.],
    #     [-1.87761058, 1.18289466, -1.],
    #     [-0.85812972, -0.13129385, -1.],
    #     [-1.42048733, 0.49859105, -1.],
    #     [-0.38289289, -0.36757717, -1.]])
    # q, r = qr_fact_householder(a)
    # aa, bb = qr(a)
    # print np.dot(aa, bb)
    # print np.dot(q, r)

