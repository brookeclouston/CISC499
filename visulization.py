"""
This script handles the visulization for the algoirthim 
"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
    

def plot_fittness(i):
    pullData = open("best_fitness.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar.append(int(x))
            yar.append(int(y))
    ax1.clear()
    ax1.plot(xar,yar)

#ani = animation.FuncAnimation(fig, plot_fittness, interval=1000)
#plt.show()

