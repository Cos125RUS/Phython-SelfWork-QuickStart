def membersAge(**age):
    for i, j in age.items():
        print("Name = %s, Age = %d" % (i, j))


membersAge(Peter=7, John=5)
