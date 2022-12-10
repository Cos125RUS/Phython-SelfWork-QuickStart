myDict = {"One":1.35, 2.5:"Two Point Five", 3:"+", 7.9:2}
print(myDict)
print(myDict["One"])
print(myDict[7.9])
print()

myDict[2.5] = "Two and a Half"
print(myDict)
myDict["New item"] = "I'm a new"
print(myDict)
print()

del myDict["One"]
print(myDict)
