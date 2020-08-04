import os
import time
import sys
saveCheck = os.path.isdir('Fimbulvetr Save File')
if saveCheck == False:
    os.mkdir('Fimbulvetr Save File')
print("Hvat segirthu?")
print("Cause I'm doin fine")
print("Although I will say the Fimbulvetr is quite annoying, what with all the ashfall")

inGame = False

# Function Definitions

ListA = list(["a",'"a"'," a","a "])
ListB = list(["b",'"b"'," b","b "])
ListC = list(["c",'"c"'," c","c "])
ListD = list(["d",'"d"'," d","d "])
cancel = list(["cancel","stop","back"])
yes = list(["y","yes","ye","ys","yes "," yes","sure","sur","sre","ure","yeah","yea","yeh","yah","eah","yup","yip","yes please","absolutely","yep"])
no = list(["n","no","nop","nope","not","not really","not realy","no thanks","noo","nooo","noooo","nooooo","never","nno","nnoo"])

def printFun(w):
    for char in w:
        time.sleep(0.01)
        print(char, end='')


def Menu(inGame):
    loadLoop = 0
    menuStay = 0
    menuUp = 0
    global ListA
    while menuUp == 0:
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
        if inGame == True:
            print('''
         ______
        | +==. | Exit menu and return to game. To select this option, type "D" and 
        | |   || press the [Enter] key.
        |_+=='_|
        
        ''')
        while menuStay == 0:
            loadLoop = 0
            menuChoice = str(input('''
==='''))
            if menuChoice.lower() in ListA:
                optionsCheck = os.listdir('Fimbulvetr Save File')
                optionsNum = len(optionsCheck)
                if optionsNum == 0:
                    print("I'm sorry, it appears that there are no save files on this computer.")
                else:
                    print("There are {} saved files on this computer. they are:".format(optionsNum))
                    print(optionsCheck)
                    print('''
Please enter the name of the file you would like to load, or type "cancel" to cancel loading.''')
                    while loadLoop == 0:
                        loadName = str(input("==="))
                        loadTxt = loadName + ".txt"
                        if loadName in optionsCheck:
                            while True:
                                print("Are you sure you want to load {}?".format(loadName))
                                loadSure = input("Yes/No:")
                                if loadSure.lower() in yes:
                                    print('''
Loading {}.'''.format(loadName))
                                    theGame = loadName
                                    menuStay = 1
                                    menuUp = 1
                                    loadLoop = 1
                                    break
                                elif loadSure.lower() in no:
                                    print("Load Cancelled")
                                    loadLoop = 1
                                    break
                        elif loadTxt in optionsCheck:
                            while True:
                                print("Are you sure you want to load {}?".format(loadTxt))
                                loadSure = input("Yes/No:")
                                if loadSure.lower() in yes:
                                    print('''
Loading {}.'''.format(loadTxt))
                                    theGame = loadTxt
                                    menuStay = 1
                                    menuUp = 1
                                    loadLoop = 1
                                    break
                                elif loadSure.lower() in no:
                                    print("Load Cancelled")
                                    loadLoop = 1
                                    break
                        elif loadName.lower() in cancel:
                            print("Load Cancelled")
                            break
                        else:
                            print("Please type an actual option from the list.")
            elif menuChoice in ListB:
                print("bye")
            elif menuChoice in ListC:
                print("die")
            elif menuChoice in ListD:
                print("Thanks for shopping at Kmart.")
                menuUp = 1
                menuStay = 1
            else:
                print("Type an actual option please.")


# MainGame Loop

Menu(True)
