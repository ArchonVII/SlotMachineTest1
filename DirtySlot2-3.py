import random
import time
import sys
import termcolor
from termcolor import colored
import numpy as np
# from enum import Enum
# from random import *

# starter constants
stake = 10000
jackpot = 500000000
active_bet = 0
multiplier = 1
bonus_state = 0

Reel11 = ''
Reel12 = ''
Reel13 = ''

# Create class for symbol values and build list of symbols


class Symbols:

    def __init__(self, name, character, payout, hue):
        self.name = name
        self.character = character
        self.payout = payout
        self.hue = hue

    def show(self):
        print(self.character)

    def __str__(self):
        return self.character

    def __repr__(self):
        return self.character


instances = [Symbols('Circle', "0", 5, 'red'), Symbols('Plus', "+", 10, 'cyan'), Symbols('Cross', "X", 25, 'yellow'), Symbols('Seven', "7", 250, 'green')]


# checking list


for obj in instances:
    print(obj.name, obj.character, obj.payout, obj.hue)


# Debug testing the printing of each reel with independent probabilities

ReelRow1 = random.choices(instances, [45, 35, 15, 5], k=3)
ReelMatrix = np.array(ReelRow1)


for o in range(0, 2):

    ReelRow = random.choices(instances, [45, 35, 15, 5], k=3)
#    print(ReelRow)
    ReelMatrix = np.vstack([ReelMatrix, ReelRow])


# define reel


def reel(Reel11, Reel12, Reel13):
    for symbol in (Reel11, Reel12, Reel13):
        sys.stdout.write(symbol)
        sys.stdout.flush()
        time.sleep(0.1)


reel(Reel11, Reel12, Reel13)
print(ReelMatrix)

print('\n indexing test')
print(ReelMatrix[0, 1])

SymbolTest = ReelMatrix[0, 1]
print(SymbolTest.hue)

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

# Pull the position from the Matrix

            CReel00 = ReelMatrix[0, 0]
            CReel01 = ReelMatrix[0, 1]
            CReel02 = ReelMatrix[0, 2]

# Give me the symbol

            Reel11 = CReel00.character
            Reel12 = CReel01.character
            Reel13 = CReel02.character

# Give me the color

            ColorR11 = CReel00.hue
            ColorR12 = CReel01.hue
            ColorR13 = CReel02.hue

            print("\n-----Current Bet: ${}-----\n".format(active_bet))
            for c in Reel11:
                time.sleep(0.4)
                print(" |",  colored(c, ColorR11), end=' | ', flush=True)
            for c in Reel12:
                time.sleep(0.4)
                print(" |",  colored(c, ColorR12), end=' | ', flush=True)
            for c in Reel13:
                time.sleep(0.4)
                print(" |",  colored(c, ColorR13), end=' | ', flush=True)
            print("\n")
            print("----------------------------")
        else:
            pass
            print("Try again")
        givememyfuckingmoney()

#    except (Exception):
#        pass
def givememyfuckingmoney():
    for i in range(ReelMatrix.shape[0]):
        if np.all(ReelMatrix[i]==ReelMatrix[i][0]):
            print('Row Check for Win: ', i)
    run_slots()

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
