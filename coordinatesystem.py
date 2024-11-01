import numpy as np
import convertToTikz
import tools
import convertToTikz

class CoordinateSystem:
    """This class implements a coordinate system of dimension d, which can be drawn (in a 2D space)."""
    t = 137.5
    
    def __init__(self, dimension):
        assert type(dimension) == int and dimension > 0
        self.dim = dimension
        self.standard_vectors = self.make_standard_vectors()
        self.matrix = self.make_matrix()
        self.change_column_order(self.find_order_of_axes())
        self.origin = self.make_origin()
        
    def get_dimension(self):
        """Returns the dimension of the coordinate system."""
        return self.dim
    
    def make_standard_vectors(self):
        """Returns a list of the standard vectors of the coordinate system."""
        l = list()
        i = 0
        while i < self.dim:
            j = 0
            p = list()
            while j < self.dim:
                p.append(0)
                j += 1
            p[i] = 1
            i += 1
            l.append(np.array(p, dtype=float).transpose())
        return l
    
    def make_matrix(self):
        """Returns the matrix that takes points in dimension dim and turns them into 2D points."""
        M = np.zeros((self.dim, 2), dtype=float)
        for r in range(self.dim):
            deg = (self.t)*(r)
            rad = np.radians(deg)
            x = np.cos(rad)
            y = np.sin(rad)
            column = np.array([x,y], dtype=float)
            M[r] = column
        return M.transpose()
    
    def find_order_of_axes(self):
        """Finds the order of the axes and returns a list with the permutation that will fix everything."""
        list_of_degrees = list()
        for r in range(self.dim):
            deg = (self.t)*(r) % 360
            list_of_degrees.append(deg)

        sorted_list_of_degrees = sorted(list_of_degrees)
        list_of_indices = list()
        
        for degree in sorted_list_of_degrees:
            pos = list_of_degrees.index(degree)
            list_of_indices.append(pos)

        return list_of_indices
    
    def change_column_order(self, permlist):
        """Swaps the order of the columns in the matrix so that it matches the order given by permlist."""
        M = self.matrix.transpose()
        M2 = M.copy()
        i=0
        for num in permlist:
            M[i] = M2[num]
            i += 1
        return M.transpose()    
    
    def make_origin(self):
        """Returns the origin point in dimension dim."""
        j = 0
        p = list()
        while j < self.dim:
            p.append(0)
            j += 1
        return np.array(p, dtype=float).transpose()    

    def draw_coordinate_system(self, canvas, color="black"):
        """Draws the coordinate system."""
        for k in range(len(self.standard_vectors)):
            v = self.standard_vectors[k]
            v[k] = 1.5
            self.draw_arrow(self.origin, v, canvas, color=color)   
        self.name_axes(canvas)  
        
    def draw_point(self, point, canvas, color="black"):
        """Draws the given dim-dimensional point in the 2D drawing."""
        point = self.transform_point(point)
        canvas.draw_point(point, color)
        
    def draw_line(self, p1, p2, canvas, color="black"):
        """Draws a line."""
        p1 = self.transform_point(p1)
        p2 = self.transform_point(p2)
        canvas.draw_line_segment(p1, p2, color=color)
        
    def draw_arrow(self, p1, p2, canvas, color="black"):
        """Draws an arrow from the point p1 to the point p2."""
        p1 = self.transform_point(p1)
        p2 = self.transform_point(p2)
        canvas.draw_arrow(p1,p2, color)
    
    def write_text(self, point, text, canvas):
        """Writes text."""
        point = self.transform_point(point)
        canvas.write_text(point, text)
        
    def name_axes(self, canvas):
        """Writes names next to the axes in the coordinate system."""
        i = 1 
        for k in range(len(self.standard_vectors)):
            v2 = self.standard_vectors[k].copy()
            v2[k] = 1.6
            self.write_text(v2, "x" + tools.get_sub(str(i)) , canvas)
            i += 1  
            
    def transform_point(self, point):
        """Transforms a point of dimension dim into a 2D-point."""
        return self.matrix.dot(point)
            