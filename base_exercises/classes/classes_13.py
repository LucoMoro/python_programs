#good example of inheritance & duck typing

class TextBox:
    def draw(self):
        print("TextBox.")

class DropDownList:
    def draw(self):
        print("DropDownList.")

#as long an object has a draw() method, this function will work
def draw(controls):
    for control in controls:
        control.draw()

ddl = DropDownList()
textbox = TextBox()
textbox2 = TextBox()
draw([ddl, textbox, textbox2])