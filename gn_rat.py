__author__ = 'alexstelea'
import math


import numpy
from numpy.linalg import inv


def _matrix_inverse(matrix):
    # TODO
    print inv(matrix)


def gn_rat(list_of_numbers, triple_number, number_of_iterations):
    # number of pairs
    n = len(list_of_numbers)

    # initialize B as a vector
    b = numpy.matrix([[triple_number[0]], [triple_number[1]], [triple_number[2]]])

    # initialize r as a vector of residuals
    r = []
    for i in range(n):
        x_i = list_of_numbers[i][0]
        y_i = list_of_numbers[i][1]
        rational_i = (b.item(0)*x_i/(x_i+b.item(1))) + b.item(2)
        r.append([y_i - rational_i])

    r = numpy.matrix(r)

    # initialize Jacobian of R
    list_j = []
    for i in range(n):
        x_i = list_of_numbers[i][0]
        partial_ri_b1 = -(x_i/(b.item(1) + x_i))
        partial_ri_b2 = b.item(0)*x_i/((b.item(1) + x_i)**2)
        partial_ri_b3 = -1
        list_j.append([partial_ri_b1, partial_ri_b2, partial_ri_b3])

    j = numpy.matrix(list_j)

    # repeat N times
    for i in range(number_of_iterations):
        # update the b matrix
        b = b - inv(j.T*j)*j.T*r

        # update the r matrix
        list_r = []
        for x in range(n):
            x_i = list_of_numbers[x][0]
            y_i = list_of_numbers[x][1]
            rational_i = (b.item(0)*x_i/(x_i+b.item(1))) + b.item(2)
            list_r.append([y_i - rational_i])

        r = numpy.matrix(list_r)

        # update the Jacobian of r
        list_j = []
        for l in range(n):
            x_i = list_of_numbers[l][0]
            partial_ri_b1 = -(x_i/(b.item(1) + x_i))
            partial_ri_b2 = b.item(0)*x_i/((b.item(1) + x_i)**2)
            partial_ri_b3 = -1
            list_j.append([partial_ri_b1, partial_ri_b2, partial_ri_b3])

        j = numpy.matrix(list_j)

    # output B
    print b
    return b


if __name__ == '__main__':gn_rat([(0.038,0.050),
                                  (0.194,0.127),
                                  (0.425,0.094),
                                  (0.626,0.2122),
                                  (1.253,0.2729),
                                  (2.5,0.2665),
                                  (3.740,0.3317)], (0.9, 0.2, 0.1), 5)

'''

[(x1,y1), (x2,y2)]


'''
