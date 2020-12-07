
import matplotlib.pyplot as plt
from cli_io import Betsetup, Spin, Ongoing_bet, Bankroll, SteinCliIo
from gamefunctions import *

io = SteinCliIo()
game_on = True

#---------------------------------------
#Welcome message
#---------------------------------------
io.display_welcome()

while game_on:
    #**********************************
    #Start game
    #**********************************
    set_initial_stack()
    set_objective()
    set_color()
    set_bet_value()
    set_serie()

    io.display_game_start(initial_bet)
    plt.figure()
    plt.ion()
    multiple_count = 0

    while initial_bet.get_serie() < initial_bet.get_serie():
        # clear lists
        bankroll_list.clear()
        # input initial items in lists
        bankroll_list.append(initial_bet.get_stack())
        loosing_streak = 0
        loosing_streak_list.append(0)
        spincount = 0

        continue_game = True

        while continue_game:

            #END WIN
            if bankroll.get_value() >= initial_bet.get_objective():
                print("Congrats, you beat the casino, it took", spincount, "spins, you walk away with", bankroll_list[-1],"$")
                print("The longest loosing streak was", max(loosing_streak_list), " spins in a row")
                globallist_win_loss.append("WIN")
                globallist_spicount.append(spincount)
                continue_game = False
            #END REKT
            elif bankroll.get_value() <= 0:
                print("You got rekt, it took", spincount, "spins to do so")
                print("your max bankroll was ", max(bankroll_list), "$")
                print("the longest loosing streak was", max(loosing_streak_list), "spins in a row")
                print("Go sell a kidney and come play again !")
                globallist_win_loss.append("REKT")
                globallist_spicount.append(spincount)
                continue_game = False



