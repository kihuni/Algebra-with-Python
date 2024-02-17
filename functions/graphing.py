import matplotlib.pyplot as plt

"""
xmin = -10
xmax = 10
ymin = -10
ymax = 10

fig, ax = plt.subplots()
plt.axis([xmin, xmax, ymin, ymax])
plt.show()
"""
#  display axis lines

"""
import matplotlib.pyplot as plt

xmin = -10
xmax = 10
ymin = -10
ymax = 10

fig, ax = plt.subplots()
plt.axis([xmin, xmax, ymin, ymax]) # window size
plt.plot([xmin, xmax], [0, 0], 'b') # blue x-axis
plt.plot([0, 0], [ymin, ymax], 'b') # blue y-axis

plt.show()
"""

# plot one point

import matplotlib.pyplot as plt

xmin = -10
xmax = 10
ymin = -10
ymax = 10

fig, ax = plt.subplots()
plt.axis([xmin, xmax, ymin, ymax]) # window size
plt.plot([xmin, xmax], [0, 0], 'b') # blue x-axis
plt.plot([0, 0], [ymin, ymax], 'b') # blue y-axis

plt.plot([3], [4], 'ro') # red point at (3, 4)

plt.show()
