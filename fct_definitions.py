from betclass import Bet

def welcome():
    print("Hello gambler, you are playing roulette Martingale.")
    print("Rules are simple, you change colors when you win, you double down if you loose.")
    print("Get rich or get rekt trying, can you beat the odds ?")
    print("Choose an objective, game will continue until objective is met or until you have nothing left.")
    print("******************************************")

def initial_bet_input():
    bankroll_input = -1
    # test test until valid input for bankroll
    while bankroll_input <= 0:
        bankroll_input = input("How much are you gambling? ")
        try:
            bankroll_input = int(bankroll_input)
        except ValueError:
            print("You must write a numerical value")
            bankroll_input = -1
            continue
        if bankroll_input < 0:
            print(
                "You can't sit at the table with a negative stack, do you expectus to pay you ? It's not how it works")
        elif bankroll_input == 0:
            print("We know you're broke, but it takes some to get some, type in the amount you gamble.")

    print("Sitting at the table with", bankroll_input, "$")


    #test test until valid input for objective
    objective_input = bankroll_input - 1
    while objective_input <= bankroll_input:
        objective_input = int(input("Please type in your objective : "))
        if objective_input > bankroll_input:
            break
        elif objective_input == bankroll_input:
            print("If you don't want to win money, go play scrabble")
        elif objective_input < bankroll_input:
            print("If you want to loose money what the fuck are you doing here?")
    #validate input
    print("you are aiming for a ", ((objective_input - bankroll_input) / bankroll_input * 100), "% gain. Nice !")


    #test test until valid input for color
    color_choice_input = "wrongcolor"
    while color_choice_input != "black" or color_choice_input != "red":
        color_choice_input = input("Chose your starting color (red or black) ")
        if color_choice_input == "black" or color_choice_input == "red":
            break
        else:
            print("You must choose between black or red only... Do you even know roulette?")



    # test test until valid input for bet
    bet_input = -1
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

    #store in initial_bet object
    initial_bet = Bet(bankroll_input, objective_input, color_choice_input, bet_input)
    print("class result", initial_bet.get_bankroll(), initial_bet.get_objective(), initial_bet.get_color(),
          initial_bet.get_value())

