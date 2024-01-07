'''Y = X². We want to plot 100 points on X-axis. In this case, the each and every value of Y is square of X value of the same index.'''
# Import libraries

import matplotlib.pyplot as plt
import numpy as np

# Creating vectors X and Y
y = np.linspace(-2, 2, 100)
x = y ** 2

fig = plt.figure(figsize = (10, 5))
# Create the plot
plt.plot(x, y)

# Show the plot
plt.show()
