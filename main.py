import math
import random
import matplotlib.pyplot as plt


def main():
    a = random.randint(1, 1000) * 0.001
    b = random.randint(1, 1000) * 0.001
    coordinates = [a, b]
    if math.sqrt(a ** 2 + b ** 2) < 1:
        x_inside.append(a)
        y_inside.append(b)
    else:
        x_outside.append(a)
        y_outside.append(b)


x_outside = []
y_outside = []
x_inside = []
y_inside = []
i = 0
for i in range(100000):
    main()
    i += 1

pi = (4*len(x_inside))/(len(x_inside)+len(x_outside))
print(pi)
plt.scatter(x_outside, y_outside, color = 'Blue', s=0.01)
plt.scatter(x_inside, y_inside, color = 'Red', s=0.01)
plt.suptitle('Monte Carlo Approximation: ' + r'$\pi$=' + str(pi))
plt.show()
