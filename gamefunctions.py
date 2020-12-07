from cli_io import Betsetup, Spin, Ongoing_bet, Bankroll
from random import randrange


spin = Spin()
initial_bet = Betsetup()
current_bet = Ongoing_bet()
bankroll = Bankroll()
globallist_win_loss = []
globallist_spicount = []
globallist_gamecount = []
globallist_loosingstreak = []

# Define lists
bankroll_list = []
loosing_streak_list = []  # list to find maximum streak loop
loosing_streak_loop = []
spinlist = []

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
    print("you are aiming for a ", ((objective_input - initial_bet.get_stack()) / initial_bet.get_stack() * 100), "% gain. Nice !")



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
    print("your first bet will be on {}".format(initial_bet.get_color()))

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

def set_serie():
    serie = "bao"
    serie = input("how many times do you wish to run that setup? ")
    try:
        serie = int(serie)
    except ValueError:
        print("You must write a numerical value")
    if serie < 1:
        print("you must run this at least once")
    else :
        initial_bet.set_serie(serie)
        print("All right, we are running this setup {} times.".format(initial_bet.get_serie()))


def win():
    if spin.get_color() == current_bet.get_color():
        # add the loosing streak to the list
        #loosing_streak_list.append(loosing_streak)
        #globallist_loosingstreak.append(loosing_streak_list[-1])
        # clear the loosing streak
        loosing_streak = 0
        # change color
        if current_bet.get_color() == "black":
            current_bet.set_color("red")
        elif current_bet.get_color() == "red":
            current_bet.set_color("black")
        # inject pnl in bankroll
        bankroll.set_value(current_bet.get_value())
        #bankroll_list.append(bankroll)

        # ïnitialise bet
        current_bet.set_value(initial_bet.get_value())
        #bet_list.clear()
        #bet_list.append(initial_bet.get_value())
        print("Congrats you won, your bankroll is", bankroll.get_value(), ".Switch color to ", current_bet.get_color(),
              ". Next bet will be", current_bet.get_value())

def loose():
    # add 1 to the loosing streak

    # add the loosing streak to the loop
    #loosing_streak_loop.append(loosing_streak)
    # update bankroll
    bankroll.set_value(-current_bet.get_value())
    #bankroll_list.append(bankroll)
    # update bet list (for next bet)
    current_bet.set_value(current_bet.get_value() * 2 )
    print("You lost, your bankroll is", bankroll.get_value(), "next bet will be ", current_bet.get_value())
