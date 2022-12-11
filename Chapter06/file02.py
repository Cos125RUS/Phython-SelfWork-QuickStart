j = 0
for i in range(5):
    j +=2
    print(i, ' - ', j)
    if j == 6:
        break

for i in range(5):
    j +=2
    print(i, ' - ', j)
    if j == 12:
        continue
    print('*')

