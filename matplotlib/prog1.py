import matplotlib.pyplot as p #data visualization in python
import numpy
x = numpy.array([2,3,8,12]) #points of a line
y = numpy.array([4,6,12,14])
font1 = {'family':'serif','color':'red','size':15}
font2 = {'family':'serif','color':'blue','size':15}
font3 = {'family':'serif','color':'green','size':20}
#xpt,ypt,y1pt are the points to draw a graph
p.plot(x,marker='o',ms=15,mec='k',mfc='y',linestyle='--',color="red",lw=2.5) #mfc=inside color, mec=outside
p.plot(y,marker='o',ms=15,mec='k',mfc='y',linestyle='dashed')
p.grid(linestyle="--",lw=1,color="blue")
p.xlabel("label for x axis",fontdict=font1) #font dictionary = fontdict
p.ylabel("label for y axis",fontdict=font2)
p.title("This is the title",fontdict=font3)
#p.plot(ypt,linestyle='dashed')
#p.plot(ypt,linestyle='solid')
#p.plot(ypt,linestyle='dashdot')
# p.plot(xpt,marker='o',linestyle="--",ms=20,mfc='orange',mec='k')
# p.plot(y1pt,marker='o',linestyle ="-.",ms=20,mfc='b',mec='k') #b- blue, k - black
# #p.plot(ypt,linewidth='18')
# # p.plot(xpt,marker='o',ms=20,mfc='y',mec='k') #mfc = color inside of the marker
# # #p.plot(ypt,linestyle='dashdot')                                 #mec= marker border color, ms = marker size
# # # p.plot(y1pt)
# p.xlabel("X axis",fontdict=font1)
# p.ylabel("Y axis",fontdict=font2)
# p.title("This is the title",fontdict=font3)
p.show()