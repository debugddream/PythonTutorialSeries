# conditional statements:

age = int(input("Enter your age: "))

# if (age == 0 or age < 0):
#     print("Input correct age")
# elif (age > 18):
#     print("You're allowed to drive")
# elif (age == 18):
#     print("Get a license")
# else:
#     print("You're not allowed to drive")

print("Allowed") if (age > 18) else print(
    "Get license") if (age == 18) else print("Not allowed")
