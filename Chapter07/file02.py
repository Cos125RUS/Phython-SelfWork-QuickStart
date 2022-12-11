message1 = "Global"

def myFunction():
    print("\nIn function")
    print(message1)
    message2 = "Local"
    print(message2)

myFunction()

print(message1)
message2 = "Outside the function"
print(message2)