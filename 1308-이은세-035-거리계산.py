# 내 풀이

import math as m

class main:
    def __init__(self,x_1,y_1,x_2,y_2):
        self.x_1 = x_1
        self.y_1 = y_1
        self.x_2 = x_2
        self.y_2 = y_2

    def __str__(self):
        return str(m.sqrt((self.x_1-self.x_2)**2 + (self.y_1-self.y_2)**2))
x_1 = 1
y_1 = 1

x_2 = 0
y_2 = 0

result = main(x_1, y_1, x_2, y_2)

print(result)

# 쌤 풀이

class Point:
    def __init__(self, x,y):
        self.x = x
        self.y =y

    def distance(self, v):
        return m.sqrt((self.x - v.x)**2 + (self.y-v.y)**2)
    
p1 = Point(0, 0)
p2 = Point(1, 1)

print(p1.distance(p2))