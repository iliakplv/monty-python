from random import randint
import numpy as np
import matplotlib.pyplot as plt

# plt.gca().invert_yaxis()
plt.axis('equal')
plt.axis('off')

stroke_count_u = 500
stroke_points_u = 1

stroke_count_n = 500
stroke_points_n = 1

mean = 0
std = 0.5


# Normal
def rand_n():
    return np.append([0], np.abs(np.random.normal(mean, std, size=stroke_points_n)))


# Uniform
def rand_u():
    return np.append([0], np.abs(np.random.uniform(low=-3.0, high=3.0, size=stroke_points_u)))


# for i in range(stroke_count_u):
#     x_series = rand_u()
#     y_series = rand_u()
#     plt.plot(x_series, y_series, linewidth=randint(2, 5))

for i in range(stroke_count_n):
    x_series = rand_n()
    y_series = rand_n()
    plt.plot(x_series, y_series, linewidth=randint(2, 5))

plt.show()
