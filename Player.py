class Player:
    def __init__(self, name, symbol):
        if name.isalpha():
            self.__name = name
        else:
            self.__name = "Default-" + symbol
        self.__symbol = symbol

    def getName(self):
        return self.__name

    def getSymbol(self):
        return self.__symbol

