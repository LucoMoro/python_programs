class Point:
    def move(self): #every function should have at least one parameter
        print("move")
    
    def draw(self):
        print("draw")


point1 = Point()
#point1.x = 10
#point1.y = 20
#print(point1.x)
point1.draw()
print(type(point1))
print(isinstance(point1, Point))

point2 = Point()
#point2.x = 40
#point2.y = 60