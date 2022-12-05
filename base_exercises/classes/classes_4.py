class Point:
    default_color = "red" #class level attribute, shared accross all istances of Point class

    def __init__(self, x, y): 
        self.x = x
        self.y = y

    def move(self):
        print("move")
    
    def draw(self):
        print(f"Point ({self.x}, {self.y})")


Point.default_color="yellow"
point1 = Point(10, 20)
point1.z=10
point1.draw()
print(point1.default_color)
print(Point.default_color)

point2 = Point(30, 40)
print(point2.default_color)