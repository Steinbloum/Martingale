from cli_io import Betsetup
from cli_io import SteinCliIo

initial_bet = Betsetup()

def set_initial_stack():
    bankroll_input = -1
    #test test until valid input for bankroll
    while bankroll_input <= 0:
        bankroll_input = input("How much are you gambling? ")
        try:
            bankroll_input = int(bankroll_input)
        except ValueError:
            print("You must write a numerical value")
            bankroll_input = -1
            continue
        if bankroll_input < 0:
            print("You can't sit at the table with a negative stack, do you expectus to pay you ? It's not how it works")
        elif bankroll_input == 0:
            print("We know you're broke, but it takes some to get some, type in the amount you gamble.")
    initial_bet.set_stack(bankroll_input)
    print("Sitting at the table with {} $".format(initial_bet.get_stack()))

def set_objective():
    # test test until valid input for objective
    objective_input = initial_bet.get_stack()
    print(objective_input, initial_bet.get_stack())
    while objective_input <= initial_bet.get_stack():
        objective_input = int(input("Please type in your objective : "))
        if objective_input > initial_bet.get_stack():
            break
        elif objective_input == initial_bet.get_stack():
            print("If you don't want to win money, go play scrabble")
        elif objective_input < initial_bet.get_stack():
            print("If you want to loose money what the fuck are you doing here?")
    # validate input
    initial_bet.set_objective(objective_input)
    print(objective_input, initial_bet.get_stack())
    print("you are aiming for a ", ((objective_input - initial_bet.get_stack()) / initial_bet.get_stack() * 100), "% gain. Nice !")
    print(objective_input, initial_bet.get_stack())



def set_color():
    # test test until valid input for color
    color_choice_input = "wrongcolor"
    while color_choice_input != "black" or color_choice_input != "red":
        color_choice_input = input("Chose your starting color (red or black) ")
        if color_choice_input == "black" or color_choice_input == "red":
            break
        else:
            print("You must choose between black or red only... Do you even know roulette?")
    # validate input
    initial_bet.set_color(color_choice_input)

def set_bet_value():
    # test test until valid input for bet
    bet_input = -1
    bankroll_input = initial_bet.get_stack()
    while bet_input <= 0:
        bet_input = input("Make your initial bet ")
        try:
            bet_input = int(bet_input)
        except ValueError:
            print("You must write a numerical value")
            bet_input = -1
            continue
        if bet_input > bankroll_input:
            print("You are betting more than you have, keep it real !")
            bet_input = -1
        elif bet_input == 0:
            print("You know that anything mulitplied by 0 is 0 right ?")
        elif bet_input == bankroll_input:
            print("You are all in on the first bet, this will not end well, we cannot permit it.")
            bet_input = -1

        else:
            print("you bet represents", bet_input * 100 / bankroll_input, "% of your stack")
            break
    initial_bet.set_value(bet_input)

set_initial_stack()
set_objective()
set_color()
set_bet_value()
print(initial_bet.get_stack(), initial_bet.get_objective(), initial_bet.get_color(), initial_bet.get_value())