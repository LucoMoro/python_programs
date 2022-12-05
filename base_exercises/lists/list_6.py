letters = ["a", "b", "c"]

#Add
#letters.append("d")
#letters.insert(0, "-")
#print(letters)

#Remove
#letters.pop(0) #or letters.pop()
#letters.remove("b")
#del letters[0:3] to remove a range of items
#letters.clear()
#print(letters)

#Finding index
print(letters.index("a"))
if "d" in letters:
    print(letters.index("d"))
letters.count("d")

#Sorting lists
numbers = [3, 51, 2, 8, 6]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

print(sorted(numbers)) #sorts a new list, not numbers
print(numbers)

items = [ ("Product1", 10),
("Product2", 9),
("Product3", 12),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)