import figure
import coordinatesystem

class TikzCode:
    """A class for the tikz code for drawing a given (simplex complex) figure."""
    def __init__(self, fig):
        self.fig = fig
        self.list_of_rows = self.fig.get_rows()
        self.list_of_points = self.fig.get_points()
        
        self.n = self.fig.get_dimension()
        self.sys = coordinatesystem.CoordinateSystem(self.n)
        
        for pointpos in range(len(self.list_of_points)):
            self.list_of_points[pointpos] = self.sys.transform_point(self.list_of_points[pointpos])  
            
        self.nodes = self.make_node_dictionary()
        self.code = self.make_tikz_code() 
        
    def get_code(self):
        """Returns the code."""
        return self.code
    
    def make_tikz_code(self):
        """Writes and returns the tikz code for the entire figure with coordinate system."""
        tikz_code = '\\' + 'begin{center}\n\\' + 'begin{tikzpicture}[dot/.style={draw,fill,circle,inner sep=1pt},scale=4]\n%\n'
        tikz_code += self.make_coordinate_system()
        tikz_code += '%\n%nodes\n'
        tikz_code += '\\' + 'begin{scope}[color=pptgrønn]\n'
        tikz_code += self.make_nodes()
        tikz_code += '%\n%edges\n'
        tikz_code += self.draw_facets("red")
        tikz_code += '\\' + 'end{scope}\n'
        tikz_code += '%\n\end{tikzpicture}\n\end{center}\n'
        tikz_code += '\\' + 'vspace{1cm}\n'
        tikz_code += self.write_matrix()
        tikz_code += '\\' + 'newpage'
        return tikz_code

    def make_coordinate_system(self):
        """Returns the code for drawing the coordinate system with tikz."""
        text = '%coordinate system\n' + '\\' + 'begin{scope}[->]\n'

        for k in range(self.sys.dim):
            v = self.sys.standard_vectors[k]
            v[k] = 1.5
            v2 = self.sys.transform_point(v)
            vtxt = self.make_node(v2)
            text += "\draw (0,0)--" + vtxt + ";\n"
        text += '\\' + 'end{scope}\n'
        
        for k in range(self.n):
            v = self.sys.standard_vectors[k]
            v[k] = 1.5
            v2 = self.sys.transform_point(v)
            vtxt = self.make_node(v2)
            text += '\\' + 'node[label=above:{$x_' + str(k + 1) + '$}] (k' + str(k) + ') at ' + vtxt + '{};\n'
        return text
    
    def make_node(self,point):
        """Turns a point into a string. Returns this string."""
        pointtxt = '('
        for j in range(len(point)):
            pointtxt += str(point[j])
            if j < len(point)-1:
                pointtxt += ','
        pointtxt += ')'
        return pointtxt
    
    def make_nodes(self):
        """Returns the tikz code for defining the nodes."""  
        tikz_nodes = str()
        i = 0
        for point in self.list_of_points:
            point = self.make_node(point)
            tikz_nodes += '\\' + 'node[dot] (n' + str(i) + ') at ' + point + ' {};' + '\n' 
            i += 1
        return tikz_nodes

    def make_line(self,p1, p2):
        """Returns the tikz code for drawing a line segment between two points p1 and p2."""
        p1txt = self.make_node(p1)
        p2txt = self.make_node(p2)
        text = '\draw[] ' + self.nodes[p1txt] + '--' + self.nodes[p2txt] + ";\n"
        return text
    
    def draw_facets(self, color="black"):
        """Draws the edges of all facets"""
        text=''
        points = self.fig.get_points()
        t = 0
        for p1 in points:
            for p2 in points[t:]:
                if self.fig.point_difference(p1, p2) == 1:
                    np1 = self.fig.sys.transform_point(p1)
                    np2 = self.fig.sys.transform_point(p2)
                    text += self.make_line(np1, np2)
            t += 1
        return text

    def write_matrix(self):
        """Returns the tikz code for the matrix."""
        for row in self.list_of_rows:
            for element in row:
                if element == 0:
                        row[row.index(element)] = 'a'
                if element == 1:
                        row[row.index(element)] = 'b'
                if element == "*":
                    row[row.index(element)] = '\star' #change?
                    
        text = '\\' + 'begin{center}\n'+ '\\' + 'begin{tikzpicture}\n' + '\\' + 'matrix (m)[matrix of math nodes,nodes in empty cells, left delimiter = (, right delimiter = )]\n{\n'
    
        for row in self.list_of_rows:
            for i in range(len(row)):
                text += str(row[i])
                if i < len(row)-1:
                    text +=  ' & '
                if i == len(row)-1:
                    text += ' \\\\' + '\n'
    
        text += '};\n'+ '\\'+'end{tikzpicture}\n'+'\\'+'end{center}\n'
        return text
    
    def make_node_dictionary(self):    
        nodes = {}
        i = 0
        for point in self.list_of_points:
            point = self.make_node(point)
            txt = '(n' + str(i) + ')'
            nodes[point] = txt
            i += 1
        return nodes
