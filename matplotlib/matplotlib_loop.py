import matplotlib.pyplot as plt
x=[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
y=[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
colours=['r','g','b','k']
for i in range(len(x)):
    plt.figure()
    plt.plot(x[i],y[i],colours[i])
    # Show/save figure as desired.
    plt.show()