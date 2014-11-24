# __author__ = 'alexstelea'
#
# import matplotlib.pyplot as plt
# import matplotlib.transforms as trsfm
# import matplotlib.patches as patches
# import numpy as np
# from matplotlib.widgets import Button
#
# import math
#
# class Animation2D:
#     def __init__(self, letters):
#         self.angle = 0
#         self.letters = letters
#
#     def next_slide(self, event):
#         print "next slide"
#         plt.cla
#
#     def main(self):
#         plt.axes()
#         # circle = plt.Circle((0, 0), radius=0.75, fc='g')
#         # plt.gca().add_patch(circle)
#         fig = plt.figure()
#         ax = fig.add_subplot(111)
#
#         t_start = ax.transData
#         t = trsfm.Affine2D().rotate_deg(8)
#         t_end = t_start + t
#
#
#
        # self.angle += 9
        # theta = (self.angle/180.) * np.pi
        # rotMatrix = np.array([(np.cos(theta), -np.sin(theta)), (np.sin(theta), np.cos(theta))])
#
#         newSet = []
#         for letter in self.letters:
#             line = plt.Polygon(letter, closed=True, fill=None, edgecolor='r')
#             ax.add_patch(line)
#             for segment in letter:
#                 newSet.append(rotMatrix.dot(segment))
#             # line.set_transform(t_end)
#             print newSet
#             l = plt.Polygon(newSet, closed=True, fill=None, edgecolor='g')
#             ax.add_patch(l)
#
#
#
#         plt.axis([0, 15, 0, 15])
#         rax = plt.axes([0.05, 0.7, 0.15, 0.15], axisbg="r")
#
#         btn_next = Button(rax, "next")
#         btn_next.on_clicked(self.next_slide)
#         plt.show()
#
#
#
#
#

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Button

letters = [[(0, 0), (4, 0), (4, 2), (2, 2), (2, 6), (0, 6)], [(5, 6), (5, 0),(10,0), (10,6),(8,6),(8,2),(7,2),(7,6)], [(11, 6), (15,6), (15,5), (12,1), (15,1), (15,0), (11,0), (11,1), (14,5), (11,5) ]]
angle = 0


def generate_data():
    # do calculations and stuff here
    x = np.random.randn(50)
    y = np.random.randn(50)
    return [x,y]

def update(data):
    global angle
    newSet = []

    for letter in letters:
        theta = (angle/180.) * np.pi
        rotMatrix = np.array([(np.cos(theta), -np.sin(theta)), (np.sin(theta), np.cos(theta))])

        for segment in letter:
            newSet.append(rotMatrix.dot(segment))
        # line.set_transform(t_end)
        l = plt.Polygon(newSet, closed=True, fill=None, edgecolor='g')
    if angle < 360:
        angle += 9
    else:
        angle = 0

    # mat.set_data(newSet)

    return mat


def find_center_point(points):
    x,y=zip(*points)
    return (max(x)+min(x))/2., (max(y)+min(y))/2.


def data_gen():
    while True:
        yield generate_data()

fig = plt.figure()
ax = fig.add_subplot(111)
mat = ax.plot(generate_data())
for letter in letters:
    letter_polygon = plt.Polygon(letter, closed=True, fill="r", edgecolor='r')
    ax.add_patch(letter_polygon)
    print letter_polygon.get_xy
ani = animation.FuncAnimation(fig, update, data_gen, interval=500,
                              save_count=50)

plt.axis([0, 15, 0, 15])


plt.show()


# if __name__ == '__main__': Animation2D([[(0, 0), (4, 0), (4, 2), (2, 2), (2, 6), (0, 6)], [(5, 6), (5, 0),(10,0),
# (10,6),(8,6),(8,2),(7,2),(7,6)], [(11, 6), (15,6), (15,5), (12,1), (15,1), (15,0), (11,0), (11,1), (14,5), (11,5) ]]).main()