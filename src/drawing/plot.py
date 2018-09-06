from random import randint
import matplotlib.pyplot as plt

# plt.gca().invert_yaxis()

stroke_count = 800
canvas_size = 500

for i in range(stroke_count):
    x_series = [randint(0, canvas_size), randint(0, canvas_size)]
    y_series = [randint(0, canvas_size), randint(0, canvas_size)]
    plt.plot(x_series, y_series)

plt.show()
