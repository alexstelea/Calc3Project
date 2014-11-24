__author__ = 'alexstelea'

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy

from helpers import trace, determinant, invert, create_matrix


def power_method(matrixA, initial_guess, tolerance, max_iterations):
    matrixA = numpy.array(matrixA)

    initial_guess = numpy.array(initial_guess)

    last_eigenvalue = 0

    u = numpy.dot(matrixA, initial_guess)

    current_eigenvalue = u.item(0)
    u /= float(current_eigenvalue)

    initial_guess = u
    num_iterations = 1

    while abs(current_eigenvalue - last_eigenvalue) > tolerance:

        last_eigenvalue = current_eigenvalue
        u = numpy.dot(matrixA, initial_guess)

        current_eigenvalue = u[0]
        initial_guess = u
        num_iterations += 1

        if num_iterations > max_iterations:
            return None

    return {
        "eigenvalue": current_eigenvalue,
        "eigenvector": u,
        "#iterations": num_iterations,
        "trace(A)": trace(matrixA),
        "det(A)": determinant(matrixA)
    }


def main():
    matrices = []

    while len(matrices) < 1000:
        matrices.append(create_matrix())

    inverted_matrices = [invert(m) for m in matrices]

    e = 0.00005
    maximum_runs = 100

    data = []
    for matrix in matrices:
        result_of_power_method = power_method(matrix, [1, 1], e, maximum_runs)
        if result_of_power_method:
            data.append(result_of_power_method)

    inverse_data = []
    for matrix in inverted_matrices:
        result_of_power_method = power_method(matrix, [1, 1], e, maximum_runs)
        if result_of_power_method:
            inverse_data.append(result_of_power_method)
    # print [m['#iterations'] for m in data]
    plt.subplot(2, 1, 1)

    plt.scatter([m['det(A)'] for m in data],
                [m['trace(A)'] for m in data], c=[m['#iterations'] for m in data], cmap=mpl.cm.gist_yarg)
    plt.title('Power Method')

    plt.xlabel('Determinant of A')
    plt.ylabel('Trace of A')
    plt.subplot(2, 1, 1)

    # print [m['#iterations'] for m in inverse_data]
    plt.subplot(2, 1, 2)
    plt.scatter([m['det(A)'] for m in inverse_data],
                [m['trace(A)'] for m in inverse_data],
                c=[m['#iterations'] for m in inverse_data], cmap=mpl.cm.gray)

    plt.title('Inverse of Power Method')

    plt.xlabel('Determinant of A')
    plt.ylabel('Trace of A')

    plt.show()


if __name__ == '__main__':
    main()