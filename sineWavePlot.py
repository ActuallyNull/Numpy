import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y = np.sin(x)

plt.plot(x,y, color='r')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('A Sine Wave')

plt.savefig("Other Files\\figure.png")
plt.show()