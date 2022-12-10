myName = input("Pleas enter your name: ")
myAge = input("What about your age: ")

print("Hello World, my name is", myName, "and I am", myAge, "years old.")
print()

myAge = input("Hi %s, what about your age: "%(myName))
print("Hello World, my name is", myName, "and I am", myAge, "years old.")
print()

myAge = input("Hi {}, what about your age: ".format(myName))
print("Hello World, my name is", myName, "and I am", myAge, "years old.")
print()

print("Hello World, my name is %s and I am %s years old." %(myName, myAge))
print()

print("Hello World, my name is {} and I am {} years old.".format(myName, myAge))
print()

