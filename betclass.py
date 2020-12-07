
black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]


class Bankroll:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def get_new_value(self, winnings):

        self.value += winnings



class Pnl:
    def __init__(self, pnl):
        self.pnl = pnl

    def get_pnl(self):
        return self.pnl
    def impact_pnl(self, target):
        target.get_new_value(self.pnl)












