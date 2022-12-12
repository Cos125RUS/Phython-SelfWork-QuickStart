inputFile = open('c:\\repo\Python\SelfWork\QuickStart\Chapter08\photo.jpg','rb')
outputFile = open('c:\\repo\Python\SelfWork\QuickStart\Chapter08\photo2.jpg','wb')

msg = inputFile.read(10)

while len(msg):
    outputFile.write(msg)
    msg = inputFile.read(10)

inputFile.close()
outputFile.close()