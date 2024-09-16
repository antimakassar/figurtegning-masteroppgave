from main import Window
from figure import Figure
from coordinatesystem import CoordinateSystem
import convertToTikz

def test_figure_class():
    drawing_window = Window()
    canvas = drawing_window.canvas
    
    # test_rows = [['a','b','a'],['b','b','a'],['*','*','*']]
    test_rows = [['*','a','a'], ['a','*','*']]
    fig = Figure(test_rows,canvas)
    print(fig.get_rows())
    print(fig.get_points())
    #
    fig.draw_figure(color="red")
    code = convertToTikz.TikzCode(fig)
    print(code.get_code())
    
    drawing_window.run()
    return ''

def test_coordinate_system():
    dim = 12
    coordsyst = CoordinateSystem(dim)
    print('Dimension is', coordsyst.get_dimension())
    print('Standard vectors are\n', coordsyst.make_standard_vectors())
    print('Origin is', coordsyst.make_origin())
    
    print('Transformation matrix is\n', coordsyst.make_matrix())
    print('Transpose of transformation matrix is\n', coordsyst.make_matrix().transpose())
    print(coordsyst.make_matrix().transpose()[1])
    # l = [1,2,3,4,5,6,7,8,9,10,11,0]
    # print(coordsyst.change_column_order(l))
    print(coordsyst.change_column_order(coordsyst.find_order_of_axes()))   
    
    # testpoint = np.array([[0],[0],[1],[1]])
    # scaledtestpoint = coordsyst.scale(testpoint, 2)
    # print(scaledtestpoint)
    
    # testpoints1 = [np.array([0,0,0,0]),np.array([1,0,0,0]), np.array([0,1,0,0]), np.array([0,0,1,0]), np.array([0,0,0,1])]
    
    testpoints = list(coordsyst.make_standard_vectors())
    testpoints.append(coordsyst.make_origin())
        
    drawing_window = Window()
    
    for testpoint in testpoints:
        coordsyst.draw_coordinate_system(drawing_window.canvas, color="red")
        # coordsyst.draw_point(testpoint, drawing_window.canvas, color="red")
        
        # coordsyst.draw_arrow(coordsyst.make_origin(), testpoint, drawing_window.canvas)

        # scaledtestpoint = coordsyst.scale(testpoint,1.5)
        # print('scaled test point is', scaledtestpoint)
        # coordsyst.draw_point(scaledtestpoint, drawing_window.oldcanvas)
    drawing_window.run()
    
    
    