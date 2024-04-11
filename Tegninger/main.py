import tkinter
import numpy as np
import convertToTikz
from canvas import Canvas
from coordinatesystem import CoordinateSystem
from figure import Figure
import test


def run_drawing_program():
    run_first_window()
    
def run_first_window():
    """Opens a window where you can write the elements of the matrix"""
    first_window = tkinter.Tk()
    first_window.title("This is the title of the first window")
    colnum = enter_column_or_row(first_window, 'column')
    rownum = enter_column_or_row(first_window, 'row')
    
    def f():
        colnum2 = colnum.get()
        rownum2 = rownum.get()
        first_window.destroy()
        run_second_window(colnum2,rownum2)
    
    def g():
        colnum2 = colnum.get()
        rownum2 = rownum.get()
        first_window.destroy()
        run_second_window(colnum2,rownum2)    
    
    printButton = tkinter.Button(first_window,text = "Enter", command = f)
    printButton.pack()

    first_window.bind('<Return>', g)
    
    first_window.mainloop()


def run_second_window(column_number, row_number): 
    """Opens a window where you can add entries into a matrix. Runs the program to convert to tikz.""" 
    second_window = tkinter.Tk()
    second_window.title('This is the title of the second window')
    frame1 = tkinter.Frame()
    frame1.pack()
    welcome_text = tkinter.Label(frame1, text='Welcome to the second window! Please enter the entries of the matrix :)')
    welcome_text.pack()
    
    matrix = tkinter.Frame(borderwidth=3, relief=tkinter.GROOVE)
    matrix.pack()
    entry_list = list()
    for i in range(int(column_number)):
        for j in range(int(row_number)):
            var = tkinter.StringVar()
            idk = tkinter.Label(matrix, textvariable = var)
            idk.grid(column = int(i), row = int(j))
            entry = tkinter.Entry(matrix, textvariable = var)
            entry.grid(column = int(i), row = int(j))
       
    def h():
        for j in range(int(row_number)): 
            for i in range(int(column_number)):
                value = matrix.grid_slaves(row=j, column=i)[0].get()
                # print(value)
                entry_list.append(value)
                
        row_list = turn_entry_list_into_list_of_rows(entry_list, column_number, row_number)
        second_window.destroy()
        # convertToTikz.make_tikz_code(row_list)
        make_drawing(row_list)  
               
    printButton = tkinter.Button(second_window,text = "Enter", command = h)
    printButton.pack()
      
    second_window.mainloop()  


def make_drawing(list_of_rows):
    drawing_window = Window()
    canvas = drawing_window.canvas
    fig = Figure(list_of_rows, canvas)
    # fig.draw_figure("red")
    print(fig.get_tikz())
    drawing_window.run()

def turn_entry_list_into_list_of_rows(entry_list, column_number, row_number):
    list_of_rows = list()
    for r in range(int(row_number)):
        l = list()
        for c in range(int(column_number)):
            l.append(entry_list[0])
            entry_list.pop(0)
        list_of_rows.append(l)
    return list_of_rows

def enter_column_or_row(window, name):
    frame = tkinter.Frame(window)
    frame.pack()
    
    if name == 'column':
        label = tkinter.Label(frame, text="Number of variables: ")
        label.pack(side="left")
        var = tkinter.IntVar()
        columnrownumber = tkinter.Entry(frame, textvariable=var, exportselection=0)
        columnrownumber.pack(side="left")
        return columnrownumber

    if name == 'row':
        label = tkinter.Label(frame, text="Number of facets: ")
        label.pack(side="left")
        var = tkinter.IntVar()
        columnrownumber = tkinter.Entry(frame, textvariable=var, exportselection=0)
        columnrownumber.pack(side="left")
        return columnrownumber
    else:
        return -1


class Window:
    def __init__(self):
        self.top = tkinter.Tk()
        self.top.title("Drawing :)")
        self.canvas = Canvas(self.top)
        self.top.bind("<Button-1>", self.mouse_click)

    def mouse_click(self, event):
        self.canvas.mouse_click(event)

    def run(self):
        self.top.mainloop()


if __name__ == "__main__":
    # test.test_coordinate_system()
    # test.test_figure_class()
    run_drawing_program()
    
    
    
    
    