from time import sleep
from random import randrange

import matplotlib.pyplot as plt

from betclass import Bet, Spin
from cli_io import SteinCliIo

io = SteinCliIo()


#---------------------------------------
#Welcome message
#---------------------------------------
io.display_welcome()
runbet= True


while runbet:

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

    print("Sitting at the table with", bankroll_input,"$")

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
    # validate input


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

    initial_bet = Bet(bankroll_input, objective_input, color_choice_input, bet_input)
    print("class result", initial_bet.get_bankroll(), initial_bet.get_objective(), initial_bet.get_color(), initial_bet.get_value())
    multiple_input = int(input("how many times do you want ot run this bet setup ? "))
    break







#**********************************
#Start game
#**********************************
print("**********************************************************************************")
print("You sit at the table with", initial_bet.get_bankroll(),"$, your objective is to make",
      initial_bet.get_objective(),"$. Your first bet is", initial_bet.get_value(),"$ on",initial_bet.get_color())
print("********************************************************************************* ")
print("")
sleep(3)
print("3")
sleep(1)
print("2")
sleep(1)
print("1")
sleep(1)
print("*********HERE WE GO*********")
sleep(1)
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
