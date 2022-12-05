#good multiple inheritance

class Flyer:
    def fly(self):
        print("fly")

class Swimmer:
    def swim(self):
        print("swim")

class FlyingFish(Flyer, Swimmer):
    pass

