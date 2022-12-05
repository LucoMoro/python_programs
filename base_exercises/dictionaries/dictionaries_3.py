point = { "x": 1, "y": 2}
point2 = dict(x=1,y=2)

point["z"]=20
#print(point)

for key in point:
    print(key, point[key])

for x in point.items():
    print(x)

for key, value in point.items():
    print(key, value)
