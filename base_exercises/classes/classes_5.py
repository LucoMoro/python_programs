class Point:
    def __init__(self, x, y): 
        self.x = x
        self.y = y

    #istance methods
    def move(self):
        print("move")
    
    def draw(self):
        print(f"Point ({self.x}, {self.y})")
    
    #class methods
    @classmethod
    def zero(cls):
        return cls(0, 0)


point1 = Point(10, 20)
point1.z=10
point1.draw()
point = Point.zero()
point.draw()

point2 = Point(30, 40)