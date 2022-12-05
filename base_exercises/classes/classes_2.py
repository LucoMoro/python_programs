class Point:
    def __init__(self, x, y): #methos whit __ are called magic methods
        self.x = x
        self.y = y

    def move(self):
        print("move")
    
    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point1 = Point(10, 20)
point1.z=10
point1.draw()