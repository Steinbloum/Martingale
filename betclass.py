from random import randrange

black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
class Bet:
    def __init__(self, bankroll, objective, color, value):
        self.objective = objective
        self.bankroll = bankroll
        self.color = color
        self.value = value

    def get_bankroll(self):
        return self.bankroll

    def get_objective(self):
        return self.objective

    def get_color(self):
        return self.color

    def get_value(self):
        return self.value

class Spin:
    def __init__(self, number):
        self.number = number
    def get_number(self):
        return self.number

    def get_color(self):
        if self.number in black_numbers:
            return "black"
        elif self.number in red_numbers:
            return "red"
        else:
            return "none"
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













