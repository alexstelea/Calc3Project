__author__ = 'alexstelea'
import math

import numpy
from numpy.linalg import inv, qr
from ast import literal_eval


def _matrix_inverse(matrix):
    # TODO
    print inv(matrix)


def gn_log():
    list_of_numbers = literal_eval(raw_input("List of Points: "))
    triple_number = literal_eval(raw_input("Initial guesses for Parameters: "))
    number_of_iterations = input("How many iterations? ")
    # n list of numbers
    n = len(list_of_numbers)

    # initialize B as a vector
    b = numpy.array([[triple_number[0]], [triple_number[1]], [triple_number[2]]])

    # initialize r as a vector of residuals
    r = []
    for i in range(n):
        x_i = list_of_numbers[i][0]
        y_i = list_of_numbers[i][1]
        logaritmic_i = (b.item(0) * math.log(x_i + b.item(1))) + b.item(2)
        r.append([y_i - logaritmic_i])

    r = numpy.array(r)

    # initialize Jacobian of R
    list_j = []
    for i in range(n):
        x_i = list_of_numbers[i][0]
        partial_ri_b1 = -(math.log(b.item(1) + x_i))
        partial_ri_b2 = -(b.item(0) / (b.item(1) + x_i))
        partial_ri_b3 = -1
        list_j.append([partial_ri_b1, partial_ri_b2, partial_ri_b3])

    j = numpy.array(list_j)

    # repeat N times
    for i in range(number_of_iterations):

        Q, R = qr(j)

        # set b using the new transposed method
        inverse_r_dot_q_transpose = numpy.dot(inv(R), Q.T)
        inverse_r_dot_q_transpose_dot_r = numpy.dot(inverse_r_dot_q_transpose, r)
        b = b - inverse_r_dot_q_transpose_dot_r

        # old method (just for reference)
        # b = b - inv(j.T*j)*j.T*r

        # update the r matrix
        list_r = []
        for x in range(n):
            x_i = list_of_numbers[x][0]
            y_i = list_of_numbers[x][1]
            logaritmic_i = (b.item(0) * math.log(x_i + b.item(1))) + b.item(2)
            list_r.append([y_i - logaritmic_i])

        r = numpy.array(list_r)

        # update the Jacobian of r
        list_j = []
        for l in range(n):
            x_i = list_of_numbers[l][0]
            partial_ri_b1 = -(math.log(b.item(1) + x_i))
            partial_ri_b2 = -(b.item(0) / (b.item(1) + x_i))
            partial_ri_b3 = -1
            list_j.append([partial_ri_b1, partial_ri_b2, partial_ri_b3])

        j = numpy.array(list_j)

    # output B
    print "Converges towards: "
    print b
    return b



if __name__ == '__main__':gn_log()

'''

[(x1,y1), (x2,y2)]


'''
