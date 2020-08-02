import os
import time
import sys
saveCheck = os.path.isdir('Fimbulvetr Save File')
if saveCheck == False:
    os.mkdir('Fimbulvetr Save File')
print("Hvat segirthu?")
print("Cause I'm doin fine")
print("Although I will say the Fimbulvetr is quite annoying, what with all the ashfall")

# Function Definitions

ListA = list(["A","a",'"a"','"A"'," A"," a","A ","a ",])
ListB = list(["B","b",'"b"','"B"'," B"," b","B ","b ",])
ListC = list(["C","c",'"c"','"C"'," C"," c","C ","c ",])
ListD = list(["D","d",'"d"','"D"'," D"," d","D ","d ",])

def printFun(w):
    for char in w:
        time.sleep(0.01)
        print(char, end='')
def Menu():
    global ListA
    while True:
        print('''
         __________________________________________
        |                                          |
        | |||\ /|||  H]]]]]  |///\  |/|  Hlll  Hl| |
        | |||\V/|||  H]|__   |/|\/\ |/|  Hlll  Hl| |
        | |||   |||  H]]]]]  |/| \/\|/|  Hlll  Hl| |
        | |||   |||  H]|__   |/|  \///|  HlllL/ll| |
        | |||   |||  H]]]]]  |/|   \//|   \lllll/  |
        |__________________________________________|''')
        print(''' 
        Please select ONE of the following options:
        
         ______
        |  /\  | Load Game. This will automatically save your game and load a
        | /==\ | different game instead. 
        |/____\| To select this option, please type "A" and press the [Enter] key.
         ______
        | | \  | New Game. This will create a new game file, so you can play from
        | |-<  | the beginning of the game.
        |_|__|_| To select this option, please type "B" and press the [Enter] key.
         ______
        |  ,-- | Delete Game. This will Delete a previously created game. 
        | |    | =====================>[WARNING]<=====================
        |__'--_| THIS IS IRREVERSIBLE. TO SELECT THIS OPTION, TYPE "C" AND PRESS [Enter]
        
        ''')
        while True:
            menuChoice = str(input('''
==='''))
            if menuChoice in ListA:
                optionsCheck = os.listdir('Fimbulvetr Save File')
                optionsNum = len(optionsCheck)
                if optionsNum == 0:
                    print("I'm sorry, it appears that there are no save files on this computer.")
                else:
                    print("There are {} saved files on this computer. they are:".format(optionsNum))
                    print(optionsCheck)
                    print('''
Please enter the name of the file you would like to load.''')
                    while True:
                        loadName = input("===")
                        if loadName in optionsCheck:
                            print("Time to Load!")
                        else:
                            print("Please type an actual option from the list.")
            elif menuChoice in ListB:
                print("bye")
            elif menuChoice in ListC:
                print("die")
            else:
                print("Type an actual option please.")


# MainGame Loop

Menu()
