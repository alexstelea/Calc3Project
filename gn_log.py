__author__ = 'alexstelea'
import math


import numpy
from numpy.linalg import inv


def _matrix_inverse(matrix):
    # TODO
    print inv(matrix)


def gn_log(list_of_numbers, triple_number, number_of_iterations):
    # number of pairs
    n = len(list_of_numbers)

    # initialize B as a vector
    b = numpy.matrix([[triple_number[0]], [triple_number[1]], [triple_number[2]]])

    # initialize r as a vector of residuals
    r = []
    for i in range(n):
        x_i = list_of_numbers[i][0]
        y_i = list_of_numbers[i][1]
        logaritmic_i = (b.item(0)*math.log(x_i + b.item(1))) + b.item(2)
        r.append([y_i - logaritmic_i])

    r = numpy.matrix(r)

    # initialize Jacobian of R
    list_j = []
    for i in range(n):
        x_i = list_of_numbers[i][0]
        partial_ri_b1 = -(math.log(b.item(1)+x_i))
        partial_ri_b2 = -(b.item(0)/(b.item(1) + x_i))
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
            logaritmic_i = (b.item(0)*math.log(x_i + b.item(1))) + b.item(2)
            list_r.append([y_i - logaritmic_i])

        r = numpy.matrix(list_r)

        # update the Jacobian of r
        list_j = []
        for l in range(n):
            x_i = list_of_numbers[l][0]
            partial_ri_b1 = -(math.log(b.item(1)+x_i))
            partial_ri_b2 = -(b.item(0)/(b.item(1) + x_i))
            partial_ri_b3 = -1
            list_j.append([partial_ri_b1, partial_ri_b2, partial_ri_b3])

        j = numpy.matrix(list_j)

    # output B
    print b
    return b


if __name__ == '__main__':gn_log([(0.,-4.1),
                                  (1.,-4.47),
                                  (2.,-4.79),
                                  (3.,-5.09),
                                  (4.,-5.35),
                                  (5.,-5.6),
                                  (10.,-6.6)], (-2, 10, 5), 5)

'''

[(x1,y1), (x2,y2)]


'''
