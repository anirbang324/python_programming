# #histogram
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.random.normal(100,20,80)
# plt.hist(x)
# print(x)

#a simple histogram

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()