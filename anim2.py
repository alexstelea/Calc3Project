# __author__ = 'alexstelea'
#
# """
# A simple example of an animated plot... In 3D!
# """
# import numpy as np
# import matplotlib.pyplot as plt
# import mpl_toolkits.mplot3d.axes3d as p3
# import matplotlib.animation as animation
# import mpl_toolkits.mplot3d as a3
#
# def Gen_RandLine(length, dims=2) :
# """
# Create a line using a random walk algorithm
#
#     length is the number of points for the line.
#     dims is the number of dimensions the line has.
#     """
#     lineData = np.empty((dims, length))
#     lineData[:, 0] = np.random.rand(dims)
#     for index in range(1, length) :
#         # scaling the random numbers by 0.1 so
#         # movement is small compared to position.
#         # subtraction by 0.5 is to change the range to [-0.5, 0.5]
#         # to allow a line to move backwards.
#         step = ((np.random.rand(dims) - 0.5) * 0.1)
#         lineData[:, index] = lineData[:, index-1] + step
#     return [[ 0.79365709,  0.75415614, 0.72530311],
#  [ 0.25591491,  0.29307816,  0.27873664 ],
#  [ 0.65506224,  0.61883665, 0.65461955]]
#
# def update_lines(num, dataLines, lines) :
#     pass
#     # for line, data in zip(lines, dataLines) :
#         # NOTE: there is no .set_data() for 3 dim data...
#         # line.set_data(data[0:2, :num])
#         # line.set_3d_properties(data[2,:num])
#     # return lines
#
# # Attaching 3D axis to the figure
# fig = plt.figure()
# ax = p3.Axes3D(fig)
#
# # Fifty lines of random 3-D lines
# data = [Gen_RandLine(25, 3) for index in range(50)]
# letters = [[(0, 0), (4, 0), (4, 2), (2, 2), (2, 6), (0, 6)], [(5, 6), (5, 0),(10,0), (10,6),(8,6),(8,2),(7,2),(7,6)], [(11, 6), (15,6), (15,5), (12,1), (15,1), (15,0), (11,0), (11,1), (14,5), (11,5) ]]
#
# # Creating fifty line objects.
# # NOTE: Can't pass empty arrays into 3d version of plot()
# lines = [a3.art3d.Poly3DCollection([dat])for dat in letters]
# ax.add_collection3d(lines)
#
# lines_x = []
# lines_y = []
# lines_z = []
#
# for letter in letters:
#     for segment in letter:
#         lines_x.append(segment[0])
#         lines_y.append(segment[1])
#         lines_z.append(0)
#
#
# ax.plot(lines_x, lines_y,lines_z)
# # Setting the axes properties
# ax.set_xlim3d([0.0, 20.0])
# ax.set_xlabel('X')
#
# ax.set_ylim3d([0.0, 20.0])
# ax.set_ylabel('Y')
#
# ax.set_zlim3d([-1.0, 1.0])
# ax.set_zlabel('Z')
#
# ax.set_title('3D Test')
#
# # Creating the Animation object
# line_ani = animation.FuncAnimation(fig, update_lines, 25, fargs=(data, lines),
#                               interval=50, blit=False)
#
# plt.show()

import math


import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)

letters = [[(0, 0), (4, 0), (4, 2), (2, 2), (2, 6), (0, 6)],
           [(5, 6), (5, 0), (10, 0), (10, 6), (8, 6), (8, 2), (7, 2), (7, 6)],
           [(11, 6), (15, 6), (15, 5), (12, 1), (15, 1), (15, 0), (11, 0), (11, 1), (14, 5), (11, 5)]]

ax = plt.axes(xlim=(0, 15), ylim=(0, 15))
letter_1 = plt.Polygon(letters[0], closed=True, fill=None, edgecolor="r")
letter_2 = plt.Polygon(letters[1], closed=True, fill=None, edgecolor="b")
letter_3 = plt.Polygon(letters[2], closed=True, fill=None, edgecolor="r")

angle = 0
factor = 0.7
factor_2 = 0.3

def init():
    ax.add_patch(letter_1)
    ax.add_patch(letter_2)
    ax.add_patch(letter_3)
    return letter_1, letter_2, letter_3


def rotate_point(center_point, point, angle):
    """Rotates a point around another centerPoint. Angle is in degrees.
    Rotation is counter-clockwise"""
    temp_point = point[0]-center_point[0] , point[1]-center_point[1]
    temp_point = ( temp_point[0]*math.cos(angle)-temp_point[1]*math.sin(angle) , temp_point[0]*math.sin(angle)+temp_point[1]*math.cos(angle))
    temp_point = temp_point[0]+center_point[0] , temp_point[1]+center_point[1]
    return temp_point


def rotate_point_2(center_point, point, top_left=None):
    """Rotates a point around another centerPoint"""
    temp_point = point[0]-center_point[0] , point[1]-center_point[1]
    global  factor
    # temp_point =[temp_point[0]*0.9, temp_point[1]]

    if center_point[0] - top_left[0] >= 2.3:
        factor = 0.7
    if center_point[0] - top_left[0] <= 0.05:
        factor = 1.3

    temp_point =[temp_point[0]*factor, temp_point[1]]


    # temp_point = (temp_point[0], temp_point[0]*1/2-temp_point[1])
    # temp_point = (temp_point[0], 1/2*temp_point[1])
    temp_point = temp_point[0]+center_point[0] , temp_point[1]+center_point[1]
    return temp_point

def rotate_point_3(center_point, point, top_left=None):
    """Rotates a point around another centerPoint."""
    temp_point = point[0]-center_point[0] , point[1]-center_point[1]

    global factor_2
    if top_left[1] - center_point[1] >= 2.9:
        factor_2 = 0.3
    if top_left[1] - center_point[1] <= 0.05:
        factor_2 = 1.7

    temp_point =[temp_point[0], temp_point[1]*factor_2]

    temp_point = temp_point[0]+center_point[0], temp_point[1]+center_point[1]
    return temp_point

def animate(i):
    newSet = []
    newSet2 = []
    newSet3 = []

    global angle

    # letter one rotation
    for segment in letters[0]:
        if angle < 360:
            angle += math.pi / 5
        else:
            angle = 0

        newSet.append(rotate_point((2, 3), segment, math.radians(angle)))
    letter_1.set_xy(newSet)

    # letter 2 rotation
    for segment in letters[1]:
        # rotMatrix2 = np.array([[0.9, 0], [0, 1]])
        ans = rotate_point_2((7.5, 3), segment, top_left=letters[1][0])

        newSet2.append(ans)

    letters[1] = newSet2
    letter_2.set_xy(newSet2)

    # letter 3 rotation
    for segment in letters[2]:
        newSet3.append(rotate_point_3((13, 3), segment, top_left=letters[2][0]))


    letters[2] = newSet3
    letter_3.set_xy(newSet3)

    return letter_1, letter_2, letter_3



anim = animation.FuncAnimation(fig, animate,
                               init_func=init,
                               frames=120,
                               interval=500,
                               blit=False)

anim.save('letters.mp4', fps=24)

plt.show()