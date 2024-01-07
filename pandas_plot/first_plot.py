#Pandas uses the plot() method to create diagrams.

#We can use Pyplot, a submodule of the Matplotlib library to visualize the diagram on the screen.

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('sd1.csv')  #dataframe
df.plot() #plotting using pandas
plt.show()


'''Specify that you want a scatter plot with the kind argument:

kind = 'scatter'

A scatter plot needs an x- and a y-axis.

In the example below we will use "Duration" for the x-axis and "Calories" for the y-axis.

Include the x and y arguments like this:

x = 'Duration', y = 'Calories'''

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

plt.show()


'''Let's create another scatterplot, where there is a bad relationship between the columns, like "Duration" and "Maxpulse", with the correlation 0.009403:'''

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data.csv')
df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')
plt.show()
