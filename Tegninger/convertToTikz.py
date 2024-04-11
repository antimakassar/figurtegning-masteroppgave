

def make_tikz_code(list_of_rows):
    tikz_code =  '\\' + 'begin{center}\n\\' + 'begin{tikzpicture}[scale=2]\n%\n%noder\n'
    tikz_code += make_nodes(list_of_rows)
    tikz_code += '%\n\end{tikzpicture}\n\end{center}\n'
    print(tikz_code)
    return tikz_code

def write_matrix(list_of_rows):
    for row in list_of_rows:
        for element in row:
            if element == 0:
                    row[row.index(element)] = 'a'
            if element == 1:
                    row[row.index(element)] = 'b'
            if element == "*":
                row[row.index(element)] = '*' #change?
    
    text = '\\' + 'begin{center}\n'+ '\\' + 'begin{tikzpicture}\n' + '\\' + 'matrix (m)[matrix of math nodes,nodes in empty cells, left delimiter = (, right delimiter = )]\n{\n'
    
    for row in list_of_rows:
        for i in range(len(row)):
            text += str(row[i])
            if i < len(row)-1:
                text +=  ' & '
            if i == len(row)-1:
                text += ' \\\\' + '\n'
    
    text += '};\n'+ '\\'+'end{tikzpicture}\n'+'\\'+'end{center}\n'
    return text

def make_node(point):
    pointtxt = '('
    for j in range(len(point)):
        pointtxt += str(point[j])
        if j < len(point)-1:
            pointtxt += ','
    pointtxt += ')'
    return pointtxt
    
def make_nodes(list_of_points):
    tikz_nodes = str()
    i = 0
    for row in list_of_points:
        point = '('
        for j in range(len(row)):
            point += str(row[j])
            if j < len(row)-1:
                point += ','
        point += ')'
        # print(point)
        tikz_nodes += '\\' + 'node[dot] (n' + str(i) + ') at ' + point + ' {};' + '\n' 
        i += 1
    return tikz_nodes

def make_line(p1, p2):
    p1txt = make_node(p1)
    p2txt = make_node(p2)
    text = '\draw[] ' + p1txt + '--' + p2txt + ";\n"
    return text

def make_several_lines_in_order(list_of_points):
    text = '\draw[] '
    for i in range(len(list_of_points)):
        pointtxt = make_node(list_of_points[i])
        text += pointtxt
        if i < len(list_of_points):
            text += '--'
    text += ";"  
    return text

def make_coordinate_system():
    return ''

def old_make_nodes(list_of_rows):
    tikz_nodes = str()
    i = 0
    for row in list_of_rows:
        point = '('
        for j in range(len(row)):
            if str(row[j]) == 'a':
                point += str(0)
            if str(row[j]) == 'b':
                point += str(1)
            if str(row[j]) == '*':
                tikz_nodes+= make_extra_node(point, i) #OK SÅ hvis * er det første i en linje, så er dette problematisk.
                point += str(1)
            if j < len(row)-1:
                point += ','
        point += ')'
        # print(point)
        tikz_nodes += '\\' + 'node (n' + str(i) + ') at ' + point + ' {};' + '\n' 
        i += 1
    return tikz_nodes



def make_extra_node(point, i):
    point += str(0)
    # Trenger også å få lagt til den siste parantesen
    extra_node_code = '\\' + 'node (n' + str(i) + str(i) + ') at ' + point + ' {};' + '\n' 
    return extra_node_code