__author__ = 'alexstelea'

import numpy
from numpy import linalg as LA
def qr_fact_givens(matrixA):
    m, n = matrixA.shape
    R = matrixA
    Q = [[0.0] * n for i in range(n)]
    for k in range(n):
        identity_matrix = [[float(i == j) for i in range(n)]for j in range(n)]
        x = [row[k] for row in R[k:]]
        e = [row[k] for row in identity_matrix[k:]]

        alpha = -cmp(x[0], 0) * LA.norm(x)

        u = map(lambda p, q: p + alpha * q, x, e)
        norm_u = LA.norm(u)

        v = map(lambda p: p/norm_u,u)
        

    print m,n


if __name__ == '__main__':qr_fact_givens(numpy.matrix([[1,2,3],[3,4,5],[6,7,8]]))
