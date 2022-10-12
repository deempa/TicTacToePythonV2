class Player:
    def __init__(self, name, symbol):
        if name.isalpha() and name != "":
            self.name = name
        else:
            self.name = "Default-" + symbol
        self.symbol = symbol

    def get_name(self):
        return self.name

    def get_symbol(self):
        return self.symbol

    def set_name(self, name):
        if name.isalpha() and name != "":
            self.name = name
        else:
            self.name = "Default-" + self.symbol
