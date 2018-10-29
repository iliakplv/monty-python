from random import randint
import numpy as np
import matplotlib.pyplot as plt

plt.axis('equal')
plt.axis('off')

stroke_points = 2
stroke_count = randint(3, 12)

mean = 0
std = 1.0


def rand_normal():
    return np.random.normal(mean, std, size=stroke_points)


def rand_uniform():
    return np.random.uniform(low=-1.0, high=1.0, size=stroke_points)


for i in range(stroke_count):
    x_series = rand_normal()
    y_series = rand_uniform()

    color_rnd = np.random.uniform()
    if color_rnd > 0.9:
        color = '#203080'
    elif color_rnd > 0.8:
        color = '#D02020'
    elif color_rnd > 0.7:
        color = '#D0D000'
    else:
        color = '#000000'

    plt.plot(x_series, y_series, linewidth=randint(1, 20), color=color)

plt.show()
