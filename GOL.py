# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 12:05:27 2014

@author: boggs
"""

import Geometry
import numpy as np
import Tkinter as tk

class GOL(tk.Frame):
    
    def __init__(self,dim,SEED):
        self.dim = dim
        self.plane = Geometry.Plane(dim,SEED)
        self.root = tk.Tk()
        tk.Frame.__init__(self,self.root)
        self.canvas = tk.Canvas(self.root,width=500,height=500)
        self.canvas.pack()
        self.root.mainloop()
        self.go()
        
    def draw_plane(self):
        self.rects = []
        for row in range(self.dim):
            for col in range(self.dim):
                if self.plane.plane[row][col]:                    
                    self.rects.append(self.canvas.create_rectangle(row*10,col*10,(row+1)*10,(col+1)*10,fill="black"))
                else:
                    self.rects.append(self.canvas.create_rectangle(row*10,col*10,(row+1)*10,(col+1)*10,fill="white"))
    def go(self):
        while True:
            self.draw_plane()
            self.root.update_idletasks()
            newPlane = np.zeros((self.dim,self.dim),dtype=int)
            for row in range(self.dim):
                for col in range(self.dim):
                    newPlane[row][col] = self.plane.change_cell(row,col)
            self.plane.plane = newPlane
    

            