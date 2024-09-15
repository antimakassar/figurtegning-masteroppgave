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
        self.standard_vectors = self.get_standard_vectors()
        self.matrix = self.get_matrix()
        self.origin = self.get_origin()
        
    def get_dimension(self):
        """Returns the dimension of the coordinate system."""
        return self.dim
    
    def get_standard_vectors(self):
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
    
    def get_matrix(self):
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
    
    def get_origin(self):
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

    def name_axes(self, canvas):
        """Writes names next to the axes in the coordinate system."""
        i = 1 
        for k in range(len(self.standard_vectors)):
            v2 = self.standard_vectors[k].copy()
            v2[k] = 1.6
            self.write_text(v2, "x" + tools.get_sub(str(i)) , canvas)
            i += 1   
        
    def draw_point(self, point, canvas, color="black"):
        """Draws the given dim-dimensional point in the 2D drawing."""
        point = self.transform_point(point)
        canvas.draw_point(point, color)
        #Draw 2D point.
        
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
        point = self.transform_point(point)
        canvas.write_text(point, text)
            
    def transform_point(self, point):
        """Transforms a point of dimension dim into a 2D-point."""
        return self.matrix.dot(point)
     
    # def scale(self, point, scalar):
    #     """Scales a point (as a vector) by the scalar."""
    #     #Denne gjør et eller annet galt.
    #     S = np.zeros((1,len(point)))
    #     print(point)
    #     for i in range(len(point)):
    #         point[i] = scalar*point[i]
    #     print(point)
    #     return point.transpose()
            