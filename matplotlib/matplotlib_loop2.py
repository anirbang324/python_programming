'''In the given example firstly we are importing all the necessary libraries that we are going to use. And then creating X and Y. X holds the values from 0 to 10 which evenly spaced into 100 values. e.g. we are creating values from 2 to 3 with evenly spaced 5 values (np.linspace(2, 3, 5)) It should output like these 5 values from 2 to 3 evenly spaced array([2 , 2.25, 2.5 , 2.75, 3 ]). After that we are initializing GUI using plt.ion() function, now we have to create a subplot, so we can plot X and Y values. After that we are running a for loop up to some iterations and creating a new_y values which hold our updating value then we are updating the values of X  and Y using set_xdata() and set_ydata(). And canvas.draw() will plot the updated values and canvas.flush_events() holds the GUI event till the UI events have been processed. This will run till the loop ends and values will be updated continuously.'''

# importing libraries
import numpy as np
import time
import matplotlib.pyplot as plt

# creating initial data values
# of x and y
x = np.linspace(0, 10, 100)
y = np.sin(x)

# to run GUI event loop
plt.ion()

# here we are creating sub plots
figure, ax = plt.subplots(figsize=(10, 8))
line1, = ax.plot(x, y)

# setting title
plt.title("GRAPH", fontsize=35)

# setting x-axis label and y-axis label
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Loop
for _ in range(50):
	# creating new Y values
	new_y = np.sin(x-0.5*_)

	# updating data values
	line1.set_xdata(x)
	line1.set_ydata(new_y)

	# drawing updated values
	figure.canvas.draw()

	# This will run the GUI event
	# loop until all UI events
	# currently waiting have been processed
	figure.canvas.flush_events()

	time.sleep(0.1)
