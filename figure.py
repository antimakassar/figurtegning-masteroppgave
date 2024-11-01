import numpy as np
from coordinatesystem import CoordinateSystem
from canvas import Canvas
import convertToTikz

class Figure:
    """A class for the simplex complex figures. """
    
    def __init__(self, list_of_rows, canvas, a=0, b=1):
        assert type(a) == int and type(b) == int
        assert a <= b
        assert type(canvas) == Canvas
        assert type(list_of_rows) == list
        
        self.a = a
        self.b = b
        self.star  = '*' 
        
        self.rows = self.f(list_of_rows)
        
        self.canvas = canvas
        self.n = len(list_of_rows[0])
        self.sys = CoordinateSystem(self.n)
        
    def get_rows(self):
        return self.rows

    def get_a(self):
        return self.a
    
    def get_b(self):
        return self.b
    
    def get_canvas(self):
        return self.canvas
    
    def get_dimension(self):
        return self.n

    def set_rows(self, rows):
        self.rows = rows
    
    def set_a(self, a):
        self.a = a
        
    def set_b(self, b):
        self.b = b
        
    def set_canvas(self, canvas):
        self.canvas = canvas
    
    def f(self, list_of_rows):
        """Changes 'a' to the value self.a and 'b' to the value self.b in the rows."""
        for row in list_of_rows:
            for element in row:
                if element == 'a':
                    row[row.index(element)] = self.a 
                if element == 'b':
                    row[row.index(element)] = self.b
                if element == "*":
                    row[row.index(element)] = self.star
        return list_of_rows       
                    
    def get_points_list(self):
        """Returns a list of the points as arrays, which may contain duplicates"""
        point_list = list()
        for row in self.rows:
            points = self.get_points_in_row(row)
            point_list += points
        return point_list
    
    def get_points(self):
        """Returns a list of the points as tuples, which does not contain duplicates."""
        point_set = set()
        
        for row in self.rows:
            for point in self.get_points_in_row(row):
                point_set.add(tuple(point))
        
        l = list(point_set)
        return l
    
    def get_points_in_row(self, row):
        """Returns a list of the points that you get from one row."""
        # counting stars:
        number_of_stars = 0
        star_positions = list()
        for j in range(len(row)):
            if row[j] == '*':
                number_of_stars += 1
                star_positions.append(j)
    
        if number_of_stars > 0:
            l = self.h(row, star_positions[0])
        if number_of_stars < 1:
            l = list()
            l.append(row)
    
        # turn the list points into arrays
        for listpointnum in range(len(l)):
            l[listpointnum] = np.array(l[listpointnum], dtype = float)
    
        return l
    
    def h(self, listpoint, pos):
        """Makes points when stars."""
        # counting stars:
        number_of_stars = 0
        star_positions = list()
        for j in range(len(listpoint)):
            if listpoint[j] == '*':
                number_of_stars += 1
                star_positions.append(j)
        
        l = list()
        
        for i in [self.a,self.b]:
            p = listpoint.copy()
            p[pos] = i
            l.append(p) 
        
        del star_positions[0]
                
        l2 = list()
        for point in l:
            if '*' in point:
                newl = self.h(point, star_positions[0])
                for newpoint in newl:
                    l2.append(newpoint)
            else:
                l2.append(point)
                
        return l2
    
    def draw_facets(self, color="black"):
        """Draws the edges of all facets"""
        points = self.get_points()
        for p1 in points:
            t = 0
            for p2 in points[t:]:
                if self.point_difference(p1, p2) == 1:
                    self.sys.draw_line(p1, p2, self.canvas,color=color)
    
    def draw_figure(self, color="black"):
        """Draws the figure in the coordinate system and the canvas."""
        self.sys.draw_coordinate_system(self.canvas)
        for point in self.get_points():
            self.sys.draw_point(point, self.canvas, color)
        self.draw_facets(color)
    
    def point_difference(self, p1, p2):
        """Calculates how many indices are different in the two points."""
        difference_counter= 0
        dim = len(p1)
        for r in range(dim):
            if p1[r] != p2[r]:
                difference_counter+=1
        return difference_counter
        