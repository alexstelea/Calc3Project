__author__ = 'alexstelea'

import numpy

def _matrix_inverse(matrix):
    return matrix

def gn_qua(list_of_numbers, triple_number, number_of_iterations):

    # initialize B as a vector
    b = numpy.matrix([triple_number[0], triple_number[1], triple_number[2]])
    print b

    # initialize r as a vector of residuals
    r = {}
    for i in range(0, number_of_iterations):
        x_i = list_of_numbers[i][0]
        y_i = list_of_numbers[i][1]
        quadratic_i = b.item(0)* x_i**2 + b.item(1)*x_i + b.item(2)
        r[i] = y_i - quadratic_i
    print r

    # initialize Jacobian of R

    j = numpy.matrix([1,2,3])
    for i in range(0, 3):
        for j in range(0, number_of_iterations):
            pass

    # do N times
        # β = β − (J⊤J)−1 J⊤ r.
        b = b - _matrix_inverse((j.getT()*j)) * j.getT() * r

        # For i=1,...,n,set ri =yi−fβ1,β2,β3(xi).

        # For i = 1,...,n and j = 1,2,3, set

    #output B
        print b
        return b


if  __name__ =='__main__':gn_qua([(1,2),(2,3)], (1,2,3), 2)

'''

[(x1,y1), (x2,y2)]


'''
