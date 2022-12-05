class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Bird(Animal):
    def fly(self):
        print("fly")


class Chicken(Bird): #inheritance abuse
    pass

