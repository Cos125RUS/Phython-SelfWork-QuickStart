try:
    userInput1 = int(input('n1 = '))
    userInput2 = int(input('n2 = '))
    answer = userInput1/userInput2
    print('answer = ', answer)
    myFile = open("missing.txt", 'r')
except ValueError:
    print('Error: you did not enter the number')
except ZeroDivisionError:
    print('Error: can not division by zero')
except Exception as e:
    print("Unknown error", e)
