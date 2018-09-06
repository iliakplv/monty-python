from random import randint
import numpy as np
import matplotlib.pyplot as plt

# plt.gca().invert_yaxis()
plt.axis('equal')

stroke_count = 100
canvas_size = 1000
mean = 0
std = 0.8


def rand():
    return np.random.normal(mean, std, 2)


for i in range(stroke_count):
    x_series = rand()
    y_series = rand()
    plt.plot(x_series, y_series, linewidth=randint(10, 20))

plt.show()
