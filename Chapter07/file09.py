import sys

if 'C:\\repo\Python\SelfWork\QuickStart\Chapter07' not in sys.path:
    sys.path.append('C:\\repo\Python\SelfWork\QuickStart\Chapter07')

import prime
answer = prime.checkIfPrime(13)
print(answer)