import random


class Dice:
    def roll(self):
        couple = [0, 0]
        couple[0]=random.randint(1,6)
        couple[1]=random.randint(1,6)
        return couple
        #return couple[0], couple[1] to return a tuple (couple[0], couple[1])


dice = Dice()
result= dice.roll()
print(f'({result[0]}, {result[1]})')
