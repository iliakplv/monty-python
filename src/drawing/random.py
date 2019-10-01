from random import randint
import numpy as np
import matplotlib.pyplot as plt

plt.axis('equal')
plt.axis('off')

stroke_points = 7
exponential_scale = 1.0
normal_mean = 0
normal_std = 1.0
uniform_low = -1.0
uniform_high = 1.0


def rand_exponential():
    return np.random.exponential(exponential_scale, size=stroke_points)


def rand_normal():
    return np.random.normal(normal_mean, normal_std, size=stroke_points)


def rand_uniform():
    return np.random.uniform(low=uniform_low, high=uniform_high, size=stroke_points)


def get_width():
    # return randint(1, 20)
    return 1


def get_color():
    # rnd = np.random.uniform(low=0.0, high=1.0)
    # if rnd > 0.9:
    #     return '#203080'
    # elif rnd > 0.8:
    #     return '#D02020'
    # elif rnd > 0.7:
    #     return '#D0D000'
    # else:
    #     return '#000000'
    return '#000000'


def draw():
    strokes = randint(10, 20)
    for _ in range(strokes):
        x_series = rand_exponential()
        y_series = rand_uniform()
        plt.plot(x_series, y_series, linewidth=get_width(), color=get_color())

    plt.show()


if __name__ == '__main__':
    draw()
