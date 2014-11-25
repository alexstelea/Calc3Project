__author__ = 'alexstelea'

import math

from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)

letters = [[(0, 0), (4, 0), (4, 2), (2, 2), (2, 6), (0, 6)],
           [(5, 6), (5, 0), (10, 0), (10, 6), (8, 6), (8, 2), (7, 2), (7, 6)],
           [(11, 6), (11, 0), (15, 0), (15, 1), (12, 1), (12, 2.5), (15, 2.5), (15, 3.5), (12, 3.5), (12, 5), (15, 5),
            (15, 6)]]

ax = plt.axes(xlim=(0, 15), ylim=(0, 15))
letter_0 = plt.Polygon(letters[0], closed=True, fill=None, edgecolor="r")
letter_1 = plt.Polygon(letters[1], closed=True, fill=None, edgecolor="b")
letter_2 = plt.Polygon(letters[2], closed=True, fill=None, edgecolor="r")

angle = 0
factor_1 = 0.7
factor_2 = 0.225


def init():
    ax.add_patch(letter_0)
    ax.add_patch(letter_1)
    ax.add_patch(letter_2)
    return letter_0, letter_1, letter_2


def rotate_letter_0(center_point, point, angle):
    temp_point = point[0] - center_point[0], point[1] - center_point[1]
    temp_point = (temp_point[0] * math.cos(2*angle) - temp_point[1] * math.sin(2*angle),
                  temp_point[0] * math.sin(2*angle) + temp_point[1] * math.cos(2*angle))
    temp_point = temp_point[0] + center_point[0], temp_point[1] + center_point[1]
    return temp_point


def rotate_letter_1(center_point, point, top_left=None):
    temp_point = point[0] - center_point[0], point[1] - center_point[1]
    global factor_1
    if center_point[0] - top_left[0] >= 2.3:
        factor_1 = 0.7
    if center_point[0] - top_left[0] <= 0.05:
        factor_1 = 1.3

    temp_point = [temp_point[0] * factor_1, temp_point[1]]
    temp_point = temp_point[0] + center_point[0], temp_point[1] + center_point[1]
    return temp_point


def rotate_letter_2(center_point, point, top_left=None):
    temp_point = point[0] - center_point[0], point[1] - center_point[1]

    global factor_2
    if top_left[1] - center_point[1] >= 2.9:
        factor_2 = 0.225
    if top_left[1] - center_point[1] <= 0.05:
        factor_2 = 1.775

    temp_point = [temp_point[0], temp_point[1] * factor_2]

    temp_point = temp_point[0] + center_point[0], temp_point[1] + center_point[1]
    return temp_point


def animate(i):
    letter_0_data = []
    letter_1_data = []
    letter_2_data = []
    global angle

    # letter 0 rotation
    for segment in letters[0]:
        if angle < 360:
            angle += math.pi / 4.15
        else:
            angle = 0
        letter_0_data.append(rotate_letter_0((2, 3), segment, math.radians(angle)))
    letter_0.set_xy(letter_0_data)

    # letter 1 rotation
    for segment in letters[1]:
        letter_1_data.append(rotate_letter_1((7.5, 3), segment, top_left=letters[1][0]))
    letters[1] = letter_1_data
    letter_1.set_xy(letter_1_data)

    # letter 2 rotation
    for segment in letters[2]:
        letter_2_data.append(rotate_letter_2((13, 3), segment, top_left=letters[2][0]))
    letters[2] = letter_2_data
    letter_2.set_xy(letter_2_data)

    return letter_0, letter_1, letter_2


anim = animation.FuncAnimation(fig, animate,
                               init_func=init,
                               frames=120,
                               interval=500,
                               blit=False)

anim.save('letters.mp4', fps=24)

plt.show()

