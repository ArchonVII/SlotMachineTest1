import random
import time
import sys
import termcolor
from termcolor import colored
import numpy as np
import tkinter as tk


# gui stuff

window = tk.Tk()
frame = tk.frame()
frame2 = tk.frame()

label = tk.Label(master=frame,
    text="Welcome to Dirty Slot \n Please Enter Your Name",
    fg="red",
    bg="black",
    width=20,
    height=5
)
label.pack()

entry = tk.Entry(master=frame2,fg="red", bg="white", width=50)
entry.pack()

frame.pack()
frame2.pack()

window.mainloop()

name = entry.get()


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

ReelMatrix = np.empty(3)

class Symbols:

    def __init__(self, name, character, payout, hue, Attr):
        self.name = name
        self.character = character
        self.payout = payout
        self.hue = hue
        self.Attr = Attr

    def show(self):
        print(self.character)

    def __str__(self):
        return self.character

    def __repr__(self):
        return self.character


instances = [Symbols('Circle', "0", 50, 'red', 'bold'), Symbols('Plus', "+", 100, 'cyan', 'bold'), Symbols('Cross', "X", 250, 'yellow', 'bold'), Symbols('Seven', "7", 1000, 'green', 'blink')]


# checking list


# for obj in instances:
#    print(obj.name, obj.character, obj.payout, obj.hue)


# Debug testing the printing of each reel with independent probabilities

# ReelRow1 = random.choices(instances, [45, 35, 15, 5], k=3)
# ReelMatrix = np.array(ReelRow1)





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

# Pull the handle


            ReelRow1 = random.choices(instances, [45, 35, 15, 5], k=3)
            ReelMatrix = np.array(ReelRow1)

            for o in range(0, 2):
                ReelRow = random.choices(instances, [45, 35, 15, 5], k=3)
                ReelMatrix = np.vstack([ReelMatrix, ReelRow])

# Pull the position from the Matrix

            CReel00 = ReelMatrix[0, 0]
            CReel01 = ReelMatrix[0, 1]
            CReel02 = ReelMatrix[0, 2]
            CReel10 = ReelMatrix[1, 0]

            CReel11 = ReelMatrix[1, 1]
            CReel12 = ReelMatrix[1, 2]
            CReel20 = ReelMatrix[2, 0]
            CReel21 = ReelMatrix[2, 1]
            CReel22 = ReelMatrix[2, 2]


# Give me the symbol

            Reel11 = CReel00.character
            Reel12 = CReel01.character
            Reel13 = CReel02.character
            Reel21 = CReel10.character
            Reel22 = CReel11.character
            Reel23 = CReel12.character
            Reel31 = CReel20.character
            Reel32 = CReel21.character
            Reel33 = CReel22.character

# Give me the color

            ColorR11 = CReel00.hue
            ColorR12 = CReel01.hue
            ColorR13 = CReel02.hue
            ColorR21 = CReel10.hue
            ColorR22 = CReel11.hue
            ColorR23 = CReel12.hue
            ColorR31 = CReel20.hue
            ColorR32 = CReel21.hue
            ColorR33 = CReel22.hue



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
            for c in Reel21:
                time.sleep(0.4)
                print(" |", colored(c, ColorR21), end=' | ', flush=True)
            for c in Reel22:
                time.sleep(0.4)
                print(" |", colored(c, ColorR22), end=' | ', flush=True)
            for c in Reel23:
                time.sleep(0.4)
                print(" |", colored(c, ColorR23), end=' | ', flush=True)
            print("\n")
            for c in Reel31:
                time.sleep(0.4)
                print(" |", colored(c, ColorR31), end=' | ', flush=True)
            for c in Reel32:
                time.sleep(0.4)
                print(" |", colored(c, ColorR32), end=' | ', flush=True)
            for c in Reel33:
                time.sleep(0.4)
                print(" |", colored(c, ColorR33), end=' | ', flush=True)

            print("\n")
            print("----------------------------")

        for i in range(ReelMatrix.shape[0]):
            if np.all(ReelMatrix[i] == ReelMatrix[i][0]):
                WinningSymbol = ReelMatrix[i][0]
                WinningAmount = WinningSymbol.payout
                positivebalance = WinningAmount * 3
                stake += positivebalance + active_bet

                print("You won $", positivebalance)
                print("Current Balance: $", stake)

                reviewcheck = random.randint(0, 5)
                print(reviewcheck)
                if reviewcheck == 5:
                    print("Please take a moment to review us in the AppStore.  Your chance of winning definitely won't be affected if you don't")
                else:
                    pass
                run_slots()
            else:
                pass


        else:
            pass
            print("Try again")
            print("Balance: ", stake)
#        givememyfuckingmoney()

#    except (Exception):
#        pass
# def givememyfuckingmoney():
#    for i in range(ReelMatrix.shape[0]):


def start():
    global stake
    print("\nWelcome to ", colored("Dirty Slot", 'red'))
    command = input("We've given you $10,000 to start. \n\nPRESS [ENTER] TO BEGIN ")
    if command == "":
        stake = 10000
        run_slots()
    else:
        print("Just hit enter")
        start()


start()
