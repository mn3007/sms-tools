import matplotlib.pyplot as plt
import numpy as np
from A2Part1 import genSine
from A2Part2 import genComplexSine
from A2Part3 import DFT


x = genComplexSine(4, 64)
x = genSine(1, 4, 0, 64, 1)
x = DFT(x)

# plt.plot(np.real(x))
# plt.plot(np.imag(x))
plt.plot(np.abs(x))
plt.show()
