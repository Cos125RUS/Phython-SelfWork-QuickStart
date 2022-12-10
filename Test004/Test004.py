n = 1.50
print (n)

name1 = 'Valerii'
name2 = 'Panov'
print (name1, name2)
fullName = name1 + name2
print (fullName)
name2 = name2.upper()
print (name2)
print ()

brand = 'Apple'
exchangeRate = 1.235235245
message = 'The price of this %s laptop is %d USD '\
          'and the exchange rate is %4.2f USD to 1 EUR'\
          %(brand, 1299, exchangeRate)

print (message)
print ()

newMessage = 'The price of this {0:s} laptop is {1:d} '\
             'USD and the exchange rate is {2:4.2f} USD to 1 EUR'\
             .format('Apple', 1299, 1.235235245)

print (newMessage)
print ()

newNewMessage = 'The price of this {} laptop is {} '\
             'USD and the exchange rate is {} USD to 1 EUR'\
             .format('Apple', 1299, 1.235235245)

print (newNewMessage)
print ()