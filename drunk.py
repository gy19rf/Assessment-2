# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 21:15:39 2020

@author: gy19rf (Richard Frimpong) Student ID 201377095
"""
"""
Module name: Programming for Geographical Information Analysis (Core skills)
Module code: GEOG5990M
"""


"""
This independent project allowd me to create an Agent-Based Model(ABM) by
importing some data from the website to show the movement of drunks from 
a pub in finding their way home as well as stopping their movement when 
they reach their respective homes.

"""
"""Note: The import operator function is very useful in the building agents (drunks) to move from a pub to their
 homes because it allows useful data files to be imported to the model

"""
"""
import agentframework
"""

import matplotlib
import matplotlib.animation
import matplotlib.pyplot
import agentframework
import random
import csv
#import sys

                #setting up a random seed to 1 in order to produce the same results when the model is being run.
random.seed(1)

"""
print the first step:
Initializing parameters
"""
homes = 25     #This assign parameters to homes, and number of drunks as well as house numbers to each home
drunks = []
num_of_drunks = 25
start_point = []
house_number = []

"""
Print the second step:
Setting a figure size for the model
"""                                                               
#set the figure size of the modeldisplay to 7, 7 in order to have a large view of of the model on the screen 
fig = matplotlib.pyplot.figure(figsize=(7, 7))#set the figure size of the modeldisplay to 7, 7 
                                              # in order to have a large view of of the model on the screen 
ax = fig.add_axes([0, 0, 1, 1])
carry_on = True	
	
def update(frame_number):
    
    fig.clear()   



"""
Print the third step:
Pulling environment data from the website
"""
f = open('drunk.plan.txt') #importing the downloaded data from the website  and make the houses appear on the screen.
data = csv.reader(f,quoting=csv.QUOTE_NONNUMERIC)
environment = []
for row in data:
    rowlist = []
    for value in row:
        rowlist.append(int(value))
    environment.append(rowlist)
f.close()

"""
Print the fourth step:
makes pub visible on the screen
"""
for a in range(300):
    for b in range(300):
        if environment[a][b] == 1:
            environment[a][b]= 99 #this value changes the color hue for the pubs  
            #print(a,b)
    #house numbers


print("print(len(drunks))", len(drunks))

"""
Print the fifth step: 
Creating drunks and make them know how to locate their house numbers
"""   
for i in range(num_of_drunks):
    house_number = (i + 1)*10
    print("house_number", house_number)
    drunks.append(agentframework.drunks(drunks, homes, environment, house_number))   
print("print(len(drunks))", len(drunks))

#setting up iterations to determine the number of times the code runs  
iteration = 0
numhome = 0
 
"""
 Print the sixth step:
Moving the drunks from the pub to their respective homes
 """                              
while (True):
    if (iteration % 1000 == 0):
        print("iteration",iteration) #testing the code to know how the drunks were able 
                                     #to move to thier homes through a number of iterations
    for i in range(num_of_drunks):
        # If the drunks are not at home, move
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
        break  # break was set to allow plotting of drunks, homes,and pub 
            
    iteration = iteration + 1

#for i in range(10, 260, 10):
#    drunks.append(agentframework1.drunks (drunks, homes, environment, house_number))
# 
""" 
Print the seventh step:  
   Plotting the drunks on the environment to show how drunks moves 
from the pub and stops when they reach their respective homes
"""        
matplotlib.pyplot.imshow(environment) # plotting the environment
matplotlib.pyplot.xlim(0, 300) # shows the plotting of x location of drunks by 300
matplotlib.pyplot.ylim(0, 300) # shows the plotting of y location of drunks by 300
for i in range(num_of_drunks):
    matplotlib.pyplot.scatter(drunks[i]._x,drunks[i]._y) 

matplotlib.pyplot.imshow(environment)
