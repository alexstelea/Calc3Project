__author__ = 'alexstelea'

import random

import numpy


def trace(matrixA):
    return matrixA[0][0] * matrixA[1][1]


def determinant(matrixA):
    a = matrixA[0][0]
    b = matrixA[0][1]
    c = matrixA[1][0]
    d = matrixA[1][1]
    return a*d - b*c


def invert(matrixA):
    a = matrixA[0][0]
    b = matrixA[0][1]
    c = matrixA[1][0]
    d = matrixA[1][1]

    co_factor = numpy.array([[d, -b], [-c, a]])

    return determinant(matrixA) * co_factor


def create_matrix():
    matrix = create_random_matrix(-2,2)
    if not determinant(matrix):
        return create_matrix()
    return matrix


def create_random_matrix(low, high):
    return [[random.uniform(low, high) for i in range(2)] for j in range(2)]