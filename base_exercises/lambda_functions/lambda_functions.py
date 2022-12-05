items = [ 
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


items.sort(key=lambda item:item[1]) #lambda function, a function defined in 1 line
print(items)