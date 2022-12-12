inputFile = open('c:\\repo\Python\SelfWork\QuickStart\Chapter08\doc.txt','r')
outputFile = open('c:\\repo\Python\SelfWork\QuickStart\Chapter08\doc2.txt','w')

msg = inputFile.read(10)

while len(msg):
    outputFile.write(msg)
    msg = inputFile.read(10)

inputFile.close()
outputFile.close()