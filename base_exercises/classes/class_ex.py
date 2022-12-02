class Name:
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        print(f'{self.name}: "Haloo"')


name = Name("Bleffo")
name.talk()
        