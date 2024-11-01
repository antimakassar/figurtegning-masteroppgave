import tkinter
import math
import tools
import numpy as np

class Canvas:
    def __init__(self, top):
        self.size_math = 4*1.2
        self.size_px = 0.8*min(top.winfo_screenwidth(), top.winfo_screenheight())
        self.origin_X = self.size_px/2
        self.origin_Y = self.size_px/2
        self.scale = self.size_px/self.size_math
        
        self.cv = tkinter.Canvas(top, width=self.size_px, height=self.size_px, bg="white")
        self.cv.focus_set()
        self.cv.pack()
        
    def math_to_px(self, x, y):
        X = np.rint(x*self.scale + self.origin_X)
        Y = np.rint(-(y*self.scale) + self.origin_Y)
        return X, Y

    def draw_point(self, point, color="black"):
        """2D point, please"""
        X, Y = self.math_to_px(point[0], point[1])
        self.cv.create_oval(X-1, Y-1, X+2, Y+2, fill=color, outline=color, width=3)
    
    def draw_line_segment(self, p1, p2, color="black"):
        """2D points, please"""
        X1, Y1 = self.math_to_px(p1[0], p1[1])
        X2, Y2 = self.math_to_px(p2[0], p2[1])
        self.cv.create_line(X1,Y1,X2,Y2, width=3, fill=color)
    
    def draw_arrow(self, p1, p2, color="black"):
        """2D points, please"""
        X1, Y1 = self.math_to_px(p1[0], p1[1])
        X2, Y2 = self.math_to_px(p2[0], p2[1])
        self.cv.create_line(X1,Y1,X2,Y2, width=3, fill=color, arrow=tkinter.LAST,)
        
    def write_text(self, point, text):
        """2D point, please"""
        X, Y = self.math_to_px(point[0], point[1])
        self.cv.create_text(X, Y, text=text, font=("Helvetica", 20))
        
        
        
        
        
        
        
        