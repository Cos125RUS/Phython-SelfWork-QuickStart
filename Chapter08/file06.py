docFile = open('c:\\repo\Python\SelfWork\QuickStart\Chapter08\doc2.txt','w')
jpgFile = open('c:\\repo\Python\SelfWork\QuickStart\Chapter08\photo2.jpg','wb')

docFile.rename('doc2.txt', 'doc3.txt')
docFile.remove('doc2.txt')

docFile.close()
jpgFile.close()
