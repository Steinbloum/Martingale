from random import randrange
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

