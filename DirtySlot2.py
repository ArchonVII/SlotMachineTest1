import random
import time
import sys
# import termcolor
# from termcolor import colored
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


print("Debug part 1")


class Symbols:

    def __init__(self, name, character, payout=0):
        self.name = name
        self.character = character
        self.payout = payout

    def show(self):
        print(self.character)

    def __str__(self):
        return self.character
    def __repr__(self):
        return self.character

instances = [Symbols('Circle', "0", 5), Symbols('Plus', "+", 10), Symbols('Cross', "X", 25), Symbols('Seven', "7", 250)]

for obj in instances:
    print(obj.name, obj.character, obj.payout)

SymbolChoice = random.choice(instances)
print(SymbolChoice.name)

for o in range(0, 3):

    ReelRow = random.choices(instances, [45, 35, 15, 5], k=3)
    print(ReelRow)


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

#            print(random.choices(instances, cum_weights=[45, 35, 15, 5]),  )
            SymbolChoice11 = random.choice(instances)
            SymbolChoice12 = random.choice(instances)
            SymbolChoice13 = random.choice(instances)

            Reel11 = SymbolChoice11.character
            Reel12 = SymbolChoice12.character
            Reel13 = SymbolChoice13.character

            print("\n-----Current Bet: ${}-----\n".format(active_bet))
            for c in Reel11:
                time.sleep(0.4)
                print(" |",  c, end=' | ', flush=True)
            for c in Reel12:
                time.sleep(0.4)
                print(" |",  c, end=' | ', flush=True)
            for c in Reel13:
                time.sleep(0.4)
                print(" |",  c, end=' | ', flush=True)
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
