# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 00:00:42 2014

@author: boggs
"""
from numpy import *
from random import randint, seed

class Plane(object):
    """Creates the 2D Plane object on which the GAME OF LIFE will be played, and
    provides various functions for manipulating, reading, and displaying the field."""
    
    def __init__(self,dim,SEED):
        self.dim = dim
        seed(SEED)
        pre_cells = []
        for i in range(dim**2):
            pre_cells.append(randint(0,1))
        self.plane = array(pre_cells).reshape(dim,dim)
        
        
    def print_plane(self):
        """Prints the plane in a messy row-by-display. Note that the field is displayed at a 90 angle using this method"""
        for row in self.plane:
            print row
            
    def cell_value(self,x,y):
        """Returns the vlaue of the specified cell, as well as a list of the 
        values of neighboring cells in this format:
        [cell_value,[left bottom, left center, left top, center bottom, center top, right bottom, right center, right top]]"""
        x-=1
        y-=1
        ops = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        nbors = []
        for op in ops:
            nborX = x+op[0]
            nborY = y+op[1]
            nbors.append(self.plane[nborX][nborY])
        return [self.plane[x][y],nbors]
        
    def change_cell(self,x,y):
        """Attempts to change the value of a cell. If the cell changes value, returns
        True, if the value remains the same, reurns False."""
        cData = self.cell_value(x,y)
        cVal = cData[0]
        nbors = cData[1]
        lives = sum(nbors)
        if cVal:
            if lives < 2:
                val = 0
            elif lives > 3:
                val = 0
            else:
                val = cVal
        elif not cVal:
            if lives ==3:
                val = 1
            else:val = cVal
        return val