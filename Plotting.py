import matplotlib.pyplot as plt
#loading matplotlib data from files
#part 1 using python csv module
'''
import csv
x=[]
y=[]
with open("example.txt","r") as csvfile:
    plots=csv.reader(csvfile, delimiter=",")
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))
plt.plot(x,y,label="Loaded from file")
'''

#part 2 using numpy
import numpy as np
x,y=np.loadtxt("example.txt", delimiter=",", unpack=True)
#above only works for two variables

plt.plot(x,y,label="Loaded from file")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Interesting Graph\n Added Newline")
plt.legend()
plt.show()
