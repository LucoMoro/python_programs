first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z":1}
print(combined) #x has 2 values, so it saves only the last one