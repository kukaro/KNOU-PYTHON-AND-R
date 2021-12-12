import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(100)
y = np.random.randn(100)

plt.plot(y, 'b:')
plt.title('Blue Dotted Line')
plt.ioff()
plt.figure()
plt.plot(y, 'g-')
plt.title('Green Solid Line')
plt.show()