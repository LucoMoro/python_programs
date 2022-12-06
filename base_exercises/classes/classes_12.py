#good example of inheritance & polymorphism

from abc import ABC, abstractmethod


class UIControl(ABC): #Stream is an abstract class

    @abstractmethod
    def draw(self): #abstract method that need to be defined in every class sub of Stream
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox.")

class DropDownList(UIControl):
    def draw(self):
        print("DropDownList.")

def draw(controls):
    for control in controls:
        control.draw()

ddl = DropDownList()
textbox = TextBox()
textbox2 = TextBox()
print(isinstance(ddl, UIControl))
#draw(ddl)
#draw(textbox)
draw([ddl, textbox, textbox2])