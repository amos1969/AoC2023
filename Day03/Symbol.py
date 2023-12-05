class Symbol:
    def __init__(self, symbol, position):
        self.symbol = symbol
        self.position = position

    def __repr__(self):
        return f"Symbol: {self.symbol} at: {self.position}"