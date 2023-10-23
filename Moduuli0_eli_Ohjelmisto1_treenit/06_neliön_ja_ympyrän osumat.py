import random
import math
# radius of the circle
circle_r = 10
# center of the circle (x, y)
circle_x = 5
circle_y = 7
value = float(input("Anna pisteiden määrä:"))
# random angle
alpha = value * math.pi * random.uniform(-1, 1)
# random radius
r = circle_r * math.sqrt(random.uniform(0, 1))
# calculating coordinates
x = r * math.cos(alpha) + circle_x
y = r * math.sin(alpha) + circle_y

print("Random point", (x, y))