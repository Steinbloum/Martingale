from random import randrange

import matplotlib.pyplot as plt

from betclass import Bet, Spin
from cli_io import SteinCliIo
from gamefunctions import *

io = SteinCliIo()


#---------------------------------------
#Welcome message
#---------------------------------------




io.display_welcome()













#**********************************
#Start game
#**********************************
io.display_game_start(initial_bet)
multiple_input = int(input("how many times do you want ot run this bet setup ? "))
plt.figure()
plt.ion()
multiple_count = 0
while multiple_count <= multiple_input:


    #Define lists
    winnings_list = []
    bankroll_list = []
    loosing_streak_list = []#list to find maximum streak loop
    loosing_streak_loop = []
    bet_list = []
    color_list_choice = []
    color_list_draw = []
    spinlist = []

    #input initial items in lists

    color_list_choice.append(initial_bet.get_color())
    bet_list.append(initial_bet.get_value())
    bankroll_list.append(initial_bet.get_bankroll())

    #set variables

    starting_bet = initial_bet.get_value()
    bankroll = initial_bet.get_bankroll()
    objective = initial_bet.get_objective()
    loosing_streak = 0


    spin = Spin(int(randrange(37)))
    spincount = 0


    continue_game = True

    while continue_game:


        #add values to lists
        spincount +=1
        spinlist.append(spincount)
        if spincount < 2:
            winnings_list.append(0)
        else:
            winnings_list.append(bankroll_list[-1] - bankroll_list[-2])
        print("bklistcnt", len(bankroll_list))
        print("spinliscnt", len(spinlist))


        #END if objective complete
        if bankroll_list[-1] >= objective:
            print("Congrats, you beat the casino, it took", spincount, "spins, you walk away with", bankroll_list[-1],"$")
            print("The longest loosing streak was", max(loosing_streak_list), " spins in a row")
            continue_game = False

        #END if REKT
        elif bankroll_list[-1] <= 0:
            print("You got rekt, it took", spincount, "spins to do so")
            print("your max bankroll was ", max(bankroll_list), "$")
            print("the longest loosing streak was", max(loosing_streak_list), "spins in a row")
            print("Go sell a kidney and come play again !")
            continue_game = False

        #Spin if conditions ok
        else:
            #go all in if not enough to double down
            if bankroll_list[-1] < bet_list[-1]:
                bet_list.append(bankroll)
                print("you don't have enough for that bet, you go all in with", bankroll)
                del spinlist[-1]
            #SPIN AND PRAY
            else:
                bet_played = bet_list[-1]
                color_played = color_list_choice[-1]
                print("You bet", bet_played, "on", color_played, ".")

                spin = Spin(int(randrange(37)))
                print("winning color is",spin.get_color())

                #add the winning color to the list
                color_list_draw.append(spin.get_color())
                winning_color = spin.get_color()

                #************
                #IF WIN
                #************

                if spin.get_color() == color_played:
                    #add the loosing streak to the list
                    loosing_streak_list.append(loosing_streak)
                    #clear the loosing streak
                    loosing_streak = 0
                    #change color
                    if color_played == "black":
                        color_list_choice.append("red")
                    elif color_played == "red":
                        color_list_choice.append("black")
                    #inject pnl in bankroll
                    bankroll += bet_list[-1]
                    bankroll_list.append(bankroll)


                    #ïnitialise bet
                    bet_played = bet_list[0]
                    bet_list.clear()
                    bet_list.append(initial_bet.get_value())
                    print("Congrats you won, your bankroll is", bankroll_list[-1], ".Switch color to ", color_list_choice[-1], ". Next bet will be", initial_bet.get_value())

                #*************
                #IF LOST
                #*************

                elif winning_color != color_played:
                    #add 1 to the loosing streak
                    loosing_streak += 1
                    #add the loosing streak to the loop
                    loosing_streak_loop.append(loosing_streak)
                    #update bankroll
                    bankroll -= bet_list[-1]
                    bankroll_list.append(bankroll)
                    #update bet list (for next bet)
                    bet_list.append(bet_played * 2 )
                    print("You lost, your bankroll is", bankroll, "next bet will be ", bet_list[-1])

                print("*********************************************")



    plt.plot(20,30, spinlist, bankroll_list)
    plt.title("Bankroll evolution")
    plt.xlabel("Spin count")
    plt.ylabel("Bankroll")
    plt.pause(0.1)
    multiple_count += 1
    plt.show()
