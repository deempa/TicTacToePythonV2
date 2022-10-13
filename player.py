class Player:
    def __init__(self, name, symbol):
        self.symbol = symbol
        self.name = name
        self.set_name(name)

    def get_name(self):
        return self.name

    def get_symbol(self):
        return self.symbol

    def set_name(self, name):
        if name.isalpha() and name != "":
            self.name = name
        else:
            self.name = "Default-" + self.symbol
