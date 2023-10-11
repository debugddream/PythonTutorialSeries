"""
i = 0
while (i < 4):
    if (i == 3):
        i += 1
        continue
    print("Executed", i)
    i += 1
    # if (i == 3):
    #     break
else:
    print("Loop finished")
    print(1+1)
"""

list = ["Mango", "Apple", "Banana", "Cherry"]
i = 0
print(len(list))
while (i < len(list)):
    print(list[i])
    i += 1

# Repetitive:
# print(list[0])
# print(list[1])
# print(list[2])
# print(list[3])
