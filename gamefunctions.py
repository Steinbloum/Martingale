from cli_io import Betsetup

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

set_initial_stack()
set_objective()
print(initial_bet.get_stack(), initial_bet.get_objective())