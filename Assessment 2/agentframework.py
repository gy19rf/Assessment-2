# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 21:16:55 2020

@author: gy19rf (Richard Frimpong) Student ID:201377095
"""

"""
Module name: Programming for Geographical Information Analysis (Core skills) 
Module code: GEOG5990M
"""
"""
Agentframework is imported to create agents (drunks). The drunks were to move from a pub to their respective homesin the environment
e
"""
"""Note: The import operator function is very useful in the building agents to move from a pub to their
 homes because it allows useful data files to be imported to the model
"""

import random
class drunks():
   
    def __init__(self,drunks, homes, environment, house_number):
        """This function initialises the drunks
        """
        self. _x = random.randint (148, 150)
        self. _y = random.randint (152, 154)
        self.environment = environment
        self.drunks = drunks
        self.house_number = house_number
        self.arrived_home = False
        self.stopcount = 0
        
        
    def __str__(self):
        """ Returns a description of a drunks as a string of text.
        """
        return "Drunk(i=" + str(self.i)+ ", store=" + str(self.store) + ", x=" + str(self.x) + ", y=" + str(self.y) + ")" 
    
   
    
    """
    Making drunks to move from the pub to their homes
    """
    def move(self):
       
          
       
   
                
    
        if random.random() < 0.5:
            self._x = (self. _x + 1) % len(self.environment)
        
        else:
            self._x = (self. _x - 1) % len(self.environment)
            
            
        if random.random() < 0.5:
            self._y = (self. _y + 1) % len(self.environment)
        
        else:
            
            self._y = (self. _y - 1) % len(self.environment)                                                                                                                                        
        
        if random.random() < 0.5:
            self._x = (self. _x + 1) % 300
        
        else:
            self._x = (self. _x - 1) % 300
            
            
        if random.random() < 0.5:
            self._y = (self. _y + 1) % 300
            
        else:
            
            self._y = (self. _y - 1) % 300
        
    def example_Function(self, x, y):
        """ This function takes in two values x and y returns the sum of these 
        plus 2.
        parameters:
            x A value added to the result.
            y A value added to the result.
        returns:
            x + y + 2            
        """
        return x + y + 2
       