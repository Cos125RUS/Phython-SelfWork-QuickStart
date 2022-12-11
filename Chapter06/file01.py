num = [1, 2, 3, 4]
for i, n in enumerate(num):
    print(i, n)

print()
for n in enumerate(num):
    print(n)

print()
age = {'Peter': 20, 'Ann': 25}
for i in age:
    print(i)

print()
for i in age:
    print(i,age[i])

print()
for i in age:
    print("Name %s age %s" %(i,age[i]))

print()
for i,j in age.items():
    print(i,j)