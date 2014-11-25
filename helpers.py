__author__ = 'alexstelea'

import random
import math

import numpy


def norm(x):
    return math.sqrt(sum([x[i] ** 2 for i in range(len(x))]))


def trace(matrixA):
    return matrixA[0][0] + matrixA[1][1]


def determinant(matrixA):
    a = matrixA[0][0]
    b = matrixA[0][1]
    c = matrixA[1][0]
    d = matrixA[1][1]
    return a * d - b * c


def invert(matrixA):
    a = matrixA[0][0]
    b = matrixA[0][1]
    c = matrixA[1][0]
    d = matrixA[1][1]

    return determinant(matrixA)*numpy.array([[d, -b], [-c, a]])


def create_matrix():
    matrix = create_random_matrix(-2, 2)
    if not determinant(matrix):
        return create_matrix()
    return matrix


def create_random_matrix(low, high):
    return [[random.uniform(low, high) for i in range(2)] for j in range(2)]

def matrix_inverse(matrixA):
    from numpy.linalg import inv
    return inv(matrixA)

def embed_matrix(matrixA, m):
    # size of  matrices matrixA & m
    rows_A, cols_A = matrixA.shape
    row_m, col_m = m.shape

    # Reverse the order (horizontal & vertical of all the entries in m
    m = numpy.flipud(numpy.fliplr(m))

    for row in range(row_m):
        for col in range(col_m):
            matrixA[rows_A - row - 1, cols_A - col - 1] = m[row, col]
    return matrixA