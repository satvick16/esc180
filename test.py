import numpy as np
import matplotlib.pyplot as plt

# x0 = np.linspace(0, 1250, 1250)
# x1 = np.linspace(0, 550, 550)
# x2 = np.linspace(550, 1060, 510)
# x3 = np.linspace(1060, 1250, 190)

# y0 = np.zeros(1250)
# y1 = 0.3 * x1
# y2 = 165 - 0.7 * (x2 - 550)
# y3 = (x3 - 1060) - 190

# plt.plot(x0, y0)
# plt.plot(x1, y1)
# plt.plot(x2, y2)
# plt.plot(x3, y3)
# plt.show()

DIAPHRAGM_MASS = 10
POINT_LOAD = 10

point_loads = [550, 1250]
supports = [0, 1060]
diaphragms = [225, 550, 805, 1060, 1155]

c_pts = list(point_loads + supports + diaphragms)

for pt in c_pts:
    if pt in point_loads:
        pass
    if pt in supports:
        pass
    if pt in diaphragms:
        pass
