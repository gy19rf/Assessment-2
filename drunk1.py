# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 13:03:00 2020

@author: gy19rf
"""
#matplotlib.use('TkAgg')

import matplotlib
import matplotlib.animation
import matplotlib.pyplot
import agentframework1
import random
import csv
#import sys

#setting up a random seed to 1 in order to produce the same results when the model is being run.
random.seed(1)
#import requests
#import bs4

homes = 25
drunks = []
num_of_drunks = 25
start_point = []
house_number = []
                                                               
#set the figure size of the modeldisplay to 7, 7 in order to have a large view of of the model 
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])



carry_on = True	
	
def update(frame_number):
    
    fig.clear()   
#importing the downloaded data from the website  and make the houses appear on the screen.
f = open('drunk.plan.txt')
data = csv.reader(f,quoting=csv.QUOTE_NONNUMERIC)
environment = []
for row in data:
    rowlist = []
    for value in row:
        rowlist.append(int(value))
    environment.append(rowlist)
f.close()

#makes pub visible on the screen
for a in range(300):
    for b in range(300):
        if environment[a][b] == 1:
            environment[a][b]= 150
            #print(a,b)
    #house numbers


print("print(len(drunks))", len(drunks))

# Creating drunks and make them know how to locate their house numbers
for i in range(num_of_drunks):
    house_number = (i + 1)*10
    print("house_number", house_number)
    drunks.append(agentframework1.drunks(drunks, homes, environment, house_number))   
print("print(len(drunks))", len(drunks))

#setting up iterations to determine the number of times the  
iteration = 0
numhome = 0
#testing the code to know how the drunks were able to move to thier homes
while (True):
    if (iteration % 1000 == 0):
        print("iteration",iteration)
    for i in range(num_of_drunks):
        # If the drunhks are not at home, move
        #while self.arrived_home == false: 
        if drunks[i].arrived_home == False:
            drunks[i].move()
            #print(drunks[i]._x, drunks[i]._y)
            
            # Check if the drunk is home, if they are then set arrived_home to True so
            # they stay there and do not move in the next iteration
            #print("environment[drunks[i]._x][drunks[i]._y])", environment[drunks[i]._x][drunks[i]._y])
            
            if environment[drunks[i]._y][drunks[i]._x] == drunks[i].house_number:           
                drunks[i].arrived_home = True
                print("arrived_home at", drunks[i].house_number)
                numhome = numhome + 1
    #sys.exit was set to make sure that all the drunks are able to stop moving once they arrive home safely 
    if (numhome == num_of_drunks):
        #sys.exit("All drunks home") 
        print("All drunks home") 
        break   
            
    iteration = iteration + 1
#        
#    for i in range(num_of_drunks):
#    while environment[drunks[i]._x][drunks[i]._y] != homes[i]:
#        drunks[i].move()
#        print(drunks[i]._x, drunks[i]._y)

#for i in range(drunks.append(agentframework.drunks (drunks, homes, environment, xstart, ystart)))
  
#for y enumerate(environment):
 #for x value in enumerate(row): 
       #if value == 300:
        #xstart = x
        #ystart = y
        #print (xstart, ystart)
        
for i in range(10, 260, 10):
    drunks.append(agentframework1.drunks (drunks, homes, environment, house_number))
 
"""    Plotting the drunks on the environment to show how drunks moves 
from the pub to their respective homes
"""        
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.ylim(0, 300)
for i in range(num_of_drunks):
    matplotlib.pyplot.scatter(drunks[i]._x,drunks[i]._y) 

matplotlib.pyplot.imshow(environment)

#for i in range(num_of_drunks):
#        drunks[i].move()
#        drunks[i].get_drunks(house_number)
   
    
#matplotlib.pyplot.imshow(environment)
#def gen_function(b = [0]):
#    a = 0
#    global carry_on 
#    while  (carry_on) :
#        yield a			
#        a = a + 1
#matplotlib.pyplot.show()
#matplotlib.pyplot.draw()

#def run():
#   animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
#   canvas.draw()

#"""
#Print the tenth step:
#creating tkinter window, canvas, menu bar, Run model label, and link the Run model label with the run function
#"""
#root = tkinter.Tk()
#root.wm_title("Model")
##canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
##canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
#menu_bar = tkinter.Menu(root)
#root.config(menu=menu_bar)
#model_menu = tkinter.Menu(menu_bar)
#menu_bar.add_cascade(label="Model", menu=model_menu)
##model_menu.add_command(label="Run model", command=run)
#
#tkinter.mainloop()
