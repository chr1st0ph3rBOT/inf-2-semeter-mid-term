#63 8-puzzle
def search_index(p, k):
    for i in range(3):
        for j in range(3):
            if p[i][j] == k:
                return i+1, j+1
            

p = [[1,2,3],
     [4,'#',5],
     [6,7,8]]

def left():
    global p
    k = 2
    try:
        x, y = search_index(p, '#')
    except:
        return None
    p[x][y], p[x-1][y] = p[x-1][y], p[x][y]

def right():
    global p
    k = 2
    x, y = search_index(p, '#')
    try:
        p[x][y], p[x+1][y] = p[x+1][y], p[x][y]
    except:
        return None
    

def up():
    global p
    k = 2
    try:
        x, y = search_index(p, '#')
    except:
        return None
    p[x][y], p[x][y+1] = p[x][y+1], p[x][y]

def down():
    global p
    k = 2
    try:
        x, y = search_index(p, '#')
    except:
        return None
    p[x][y], p[x][y-1] = p[x][y-1], p[x][y]

left()
p