class ParentClass:
    def __init__(self):
        self.a=1
        print("Parent Class Object Created")
    def someMethod(self):
        print('Hello')

class ChildClass(ParentClass):
    def __init__(self):
        print("Child Class Object Creared")

parent = ParentClass()
child = ChildClass()

print(isinstance(parent, ParentClass))
print(isinstance(child, ParentClass))
print(isinstance(parent, ChildClass))

try:
    print(isinstance(parent, MyClass))
except:
    print("No such class")

print(issubclass(ChildClass, ParentClass))
print(issubclass(ParentClass, ParentClass))
print(issubclass(ChildClass, int))
print(issubclass(ChildClass, (int, ParentClass)))

print()
print(hasattr(parent, 'a'))
print(hasattr(parent, 'someMethod'))
print(hasattr(parent, 'b'))
