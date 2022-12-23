class A:
    def __init__(self):
        self.__x = 5
        self._y = 6


varA = A()
print(varA._y)
#varA.__x #ошибка
print(varA._A__x)