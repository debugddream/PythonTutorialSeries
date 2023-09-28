# List Methods:

list = ["Orange", "mango", "Apple", "Cherry"]

# Slicing

# print(list[:2])

# Change an index:
list[3] = "Pineapple"
# print(list)

# List addition:

# list.append(True)
# print(list)

# list.insert(3, False)
# print(list)

newlist = ["Fruits", "Veg", 123]
list.extend(newlist)
# print(list)

# print(list + newlist)


# List Remove Items:

# list.pop(3)
list.pop()  # pops out last index
# print(list)

list.remove("Fruits")
# print(list)


# Sorting:
list.sort()
# print(list)


newList = [12, 13, 58, 78, 1]
# newList.sort()
newList.sort(reverse=True)  # reverse sorting
# print(newList)

copy = list.copy()
print(copy)
