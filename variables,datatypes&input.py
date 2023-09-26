myVar = "This is a string"
doesExist = True
# print(doesExist)
# print(myVar)

integer = 123
float = 12.23

list = ["This", integer, 12.33, True, [integer, "newlist"]]
# print(list[1])
list[0] = "is"
# print(list)

tuple = ("This", integer, 12.33)  # this is
# print(tuple[0])
# tuple[0] = "is"
# print(tuple)


dict = {"name": "Hammad", "age": 22}
# print(dict["name"])
# print(dict)

sets = {"this", 123, "this", 123}
# print(sets)


# Input:

# name = input("Enter your name: ")
# print(type(name))

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter second value: "))
print("The sum is: ", num1 + num2)
