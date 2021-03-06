import matplotlib.pyplot as plt
import numpy as np 

X = np.arange(0,10)
Y = 0.05*X*X
Y2 = 0.03*X*X

plt.ylim(0,5)
plt.plot(X, Y, color='red')
plt.plot(X, Y2, color='green')
plt.fill_between(X, Y, Y2,  color='red', alpha=0.5)
plt.show()
