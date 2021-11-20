import random
import time
import sys
import termcolor
from termcolor import colored
from enum import Enum
from random import *

# starter constants
stake = 10000
jackpot = 500000000
active_bet = 0
multiplier = 1
bonus_state = 0

Reel11 = ''
Reel12 = ''
Reel13 = ''

# Create symbol class and add to a list


class Symbols:
    #    instances = []

    def __init__(self, character, payout=0):
        self.character = character
        self.payout = payout


Circle = Symbols("O", 5)
Plus = Symbols("+", 10)
Cross = Symbols("X", 25)
Seven = Symbols("7", 250)


# class ReelSymbol(Enum):
#    Circle = "0"
#    LetterX = "X"
#    Plus = "+"
#    LetterJ = "J"


# payout = {
#    ReelSymbol.Circle: 2,
#    ReelSymbol.LetterX: 5,
#    ReelSymbol.Plus: 20,
#    ReelSymbol.LetterJ: 100
# }


# define reel
def reel(Reel11, Reel12, Reel13):
    for symbol in (Reel11, Reel12, Reel13):
        sys.stdout.write(symbol)
        sys.stdout.flush()
        time.sleep(0.1)


reel(Reel11, Reel12, Reel13)


def run_slots():
    global Reel11, Reel12, Reel13, stake, active_bet
    while stake > 0:
        if 0 < active_bet <= stake:
            bet_r = input("\n[Enter] to repeat bet, 'No' to place new one: ")
            if bet_r == "":
                bet = active_bet
            else:
                active_bet = 0
                bet = 0
                run_slots()
        else:
            try:
                bet = int(input("Enter your bet: "))
            except ValueError:
                return run_slots()

        if 0 <= bet <= stake:
            stake -= bet
            active_bet = bet
            #            try:
            Reel11 = random.choices(Symbols.instances)
            Reel12 = random.choices(Symbols.instances)
            Reel13 = random.choices(Symbols.instances)
            print("\n-----Current Bet: ${}-----\n".format(active_bet))
            for c in Reel11:
                time.sleep(0.4)
                print(" (", "<", c, ">", end=' | ', flush=True)
            for c in Reel12:
                time.sleep(0.4)
                print(" (", "<", c, ">", end=' | ', flush=True)
            for c in Reel13:
                time.sleep(0.4)
                print(" (", "<", c, ">", end=' | ', flush=True)
            print("\n")
            print("----------------------------")
        else:
            pass
            print("Try again")


#    except (Exception):
#        pass


def start():
    global stake
    print("\nWelcome to Python Slots")
    command = input("YOU START WITH $10,000! \n\nPRESS [ENTER] TO BEGIN ")
    if command == "":
        stake = 10000
        run_slots()
    else:
        print("Just hit enter")
        start()


start()
