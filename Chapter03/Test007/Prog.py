listName = ["начальные значение"]
userAge = [21, 22, 23, 24, 25]
newListName = []

print(userAge[0])
print(userAge[1])
print(userAge[-1])
print(userAge[-2])

userAge2 = userAge
print(userAge2[2])

print()
userAge3 = userAge [2:4]
print(userAge3)

print()
userAge4 = userAge [1:5:2]
print(userAge4)

print()
print(userAge [:4])
print(userAge [1:])

print()
userAge[1] = 5
print(userAge)

print()
userAge.append(99)
print(userAge)
del userAge[2]
print(userAge)
