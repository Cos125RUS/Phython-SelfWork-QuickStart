userNameAndAge = {"Peter":38, "John":51, "Alex":13, "Alvin":"Not Available"}
userNameAndAge2 = dict(Peter = 38, John = 51, Alex = 13, Alvin = "Not Available")
print(userNameAndAge["Peter"])
print(userNameAndAge2["John"])
print()

userNameAndAge["Peter"] = 42
userNameAndAge2["John"] = 25
print(userNameAndAge)
print(userNameAndAge2)
print()

userNameAndAge3 = {}
userNameAndAge3["Joe"] = 13
print(userNameAndAge3)
userNameAndAge["Joe"] = 13
print(userNameAndAge)
del userNameAndAge["Peter"]
print(userNameAndAge)
print()
