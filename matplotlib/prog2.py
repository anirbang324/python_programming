# import numpy as np
# import matplotlib.pyplot as plt
# #grid
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
#
# plt.title("S.W.Data")
# plt.xlabel("Average")
# plt.ylabel("Calorie")
#
# plt.plot(x, y)
#
# plt.grid()
#
# plt.show()
#
# #specify which grid line to display
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(axis = 'x')

plt.show()

# #Set Line Properties for the Grid
#
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y)
plt.grid(color = 'green', linestyle = '--', linewidth = 1)
plt.show()