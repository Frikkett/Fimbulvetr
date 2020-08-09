import os
import time
import sys
saveCheck = os.path.isdir('Fimbulvetr Save File')
if saveCheck == False:
    os.mkdir('Fimbulvetr Save File')
print("Hvat segirthu?")
print("Cause I'm doin fine")
print("Although I will say the Fimbulvetr is quite annoying, what with all the ashfall")

# Global Variables
inGame = False
theGame = "hi"
Navigator = 0

# Function Definitions

ListA = list(["a",'"a"'," a","a "])
ListB = list(["b",'"b"'," b","b "])
ListC = list(["c",'"c"'," c","c "])
ListD = list(["d",'"d"'," d","d "])
cancel = list(["cancel","stop","back"])
lexit = (["exit", "break", "kill", "die", "leave", " exit", "exit ", "ext", "exi", ])
yes = list(["y","yes","ye","ys","yes "," yes","sure","sur","sre","ure","yeah","yea","yeh","yah","eah","yup","yip","yes please","absolutely","yep"])
no = list(["n","no","nop","nope","not","not really","not realy","no thanks","noo","nooo","noooo","nooooo","never","nno","nnoo"])

def printFun(w):
    for char in w:
        time.sleep(0.01)
        print(char, end='')


def Menu(inGame):
    menuStay = 0
    menuUp = 0
    global ListA
    global theGame
    while menuUp == 0:
        print(r'''
        ()=============================================================================================================()
        ||   ____________________________________________________________________________________________              ||
        || ()\__/\\\\____________/\\\\______/\\\\\\\\\\\\______/\\\\________/\\\______/\\\________/\\\___\             ||
        ||  \\\_\/\\\\\\________/\\\\\\_____\/\\\////////______\/\\\\\\_____\/\\\_____\/\\\_______\/\\\___\            ||
        ||   ()\_\/\\\//\\\____/\\\//\\\_____\/\\\______________\/\\\//\\\___\/\\\_____\/\\\_______\/\\\___\           ||
        ||    \\\_\/\\\\///\\\/\\\/_\/\\\_____\/\\\\\\\\\\\\_____\/\\\\///\\\_\/\\\_____\/\\\_______\/\\\___\          ||
        ||     ()\_\/\\\__\///\\\/___\/\\\_____\/\\\////////______\/\\\__\///\\\\\\\_____\/\\\_______\/\\\___\         ||
        ||      \\\_\/\\\____\///_____\/\\\_____\/\\\______________\/\\\____\///\\\\\_____\/\\\_______\/\\\___\        ||
        ||       ()\_\/\\\_____________\/\\\_____\/\\\\\\\\\\\\_____\/\\\______\///\\\_____\/\\\\\\\\\\\\\\\___\       ||
        ||        \\\_\///______________\///______\////////////______\///_________\///______\///////////////____\      ||
        ||         ()\___________________________________________________________________________________________\     ||
        ||          \\\___________________________________________________________________________________________\    ||
        ||           ()\___________________________________________________________________________________________\   ||
        ||            \\\___________________________________________________________________________________________\  ||
        ||             ()\___________________________________________________________________________________________\ ||
        ()=============================================================================================================()''')
        print(''' 
        Please select ONE of the following options, or type "exit" if you want to exit the game.
        
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
            deadLoop = 0
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
                                    theGame = "Fimbulvetr Save File/" + loadName
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
                                    theGame = "Fimbulvetr Save File/" + loadTxt
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

            elif menuChoice.lower() in ListB:
                makeTry = True
                while makeTry == True:
                    print("What would you like to call your game? (type 'Cancel' to exit)")
                    gameName = str(input())
                    gameDef = "Fimbulvetr Save File/" + gameName + ".txt"
                    try:
                        if gameName in cancel:
                            print("Cancelled.")
                            makeTry = False
                        else:
                            makeNew = open(gameDef, "x")
                            makeNew.close()
                            makeNew = open(gameDef, "w")
                            makeNew.write("1")
                            makeNew.close()
                            print("Your game is called {}.".format(gameName))
                            print("Your game is located at {}.".format(gameDef))
                            print('''
Please Enjoy the game.''')
                            theGame = gameDef
                            menuUp = 1
                            menuStay = 1
                            makeTry = False
                    except FileExistsError:
                        print("This name is already in use. Please choose a different name.")

            elif menuChoice.lower() in ListC:
                optionsCheck = os.listdir('Fimbulvetr Save File')
                optionsNum = len(optionsCheck)
                if optionsNum == 0:
                    print("I'm sorry, it appears that there are no save files on this computer.")
                else:
                    print("There are {} saved files on this computer. they are:".format(optionsNum))
                    print(optionsCheck)
                    print('''
Please enter the name of the file you would like to EXTERMINATE, or type "cancel" to cancel EXTERMINATION.''')
                    while deadLoop == 0:
                        deadName = str(input("==="))
                        deadTxt = deadName + ".txt"
                        if deadName in optionsCheck:
                            while True:
                                print("Are you ABSOLUTELY SURE you want to EXTERMINATE {}?".format(deadName))
                                deadSure = input("Yes/No:")
                                if deadSure.lower() in yes:
                                    print('''
Exterminate!''')
                                    time.sleep(0.2)
                                    print('''
 Exterminate!''')
                                    time.sleep(0.2)
                                    print('''
...''')
                                    time.sleep(0.2)
                                    print('''
{} Exterminated.'''.format(deadName))
                                    deleteName = "Fimbulvetr Save File/" + deadName
                                    os.remove(deleteName)
                                    deadLoop = 1
                                    break
                                elif deadSure.lower() in no:
                                    print("EXTERMINATION Cancelled")
                                    deadLoop = 1
                                    break
                        elif deadTxt in optionsCheck:
                            while True:
                                print("Are you ABSOLUTELY SURE you want to EXTERMINATE {}?".format(deadTxt))
                                deadSure = input("Yes/No:")
                                if deadSure.lower() in yes:
                                    print('''
Exterminate!''')
                                    time.sleep(0.2)
                                    print('''
Exterminate!''')
                                    time.sleep(0.2)
                                    print('''
...''')
                                    time.sleep(0.2)
                                    print('''
{} Exterminated.'''.format(deadTxt))
                                    deleteName = "Fimbulvetr Save File/" + deadTxt
                                    os.remove(deleteName)
                                    deadLoop = 1
                                    break
                                elif deadSure.lower() in no:
                                    print("EXTERMINATION Cancelled")
                                    deadLoop = 1
                                    break
                        elif deadName.lower() in cancel:
                            print("EXTERMINATION Cancelled")
                            break
                        else:
                            print("Please type an actual option from the list.")
            elif menuChoice.lower() in ListD:
                print("Thanks for shopping at Kmart.")
                menuUp = 1
                menuStay = 1
            elif menuChoice.lower() in lexit:
                print("Exiting Program.")
                exit()
            else:
                print("Type an actual option please.")


# MainGame Loop

Menu(False)
gameOn = 0
while gameOn == 0:
    segCheck = open(theGame,"r")
    Navigator = str(segCheck.readline(1))

    # NOTE TO SELF: DO NOT CHANGE THE BELOW SEGMENT. IT IS THE TEMPLATE FOR COPY AND PASTE.

    if Navigator == "0":
        print('''
        
        ''')
        while True:
            gameChoice = str(input(""))
            if gameChoice.lower() in ListA:
                print('''
            
                ''')
                Navigator = "1"
                break
            if gameChoice.lower() in ListB:
                print('''
            
                ''')
                Navigator = "1"
                break
            if gameChoice.lower() in ListC:
                print('''
            
                ''')
                Navigator = "1"
                break
            else:
                print("Please select an actual option.")

    if Navigator == "1":
        print('''
        
        
        ''')
        while True:
            gameChoice = str(input(""))
            if gameChoice.lower() in ListA:
                print('''
            
                ''')
                Navigator = "1"
                break
            if gameChoice.lower() in ListB:
                print('''
            
                ''')
                Navigator = "1"
                break
            if gameChoice.lower() in ListC:
                print('''
            
                ''')
                Navigator = "1"
                break
            else:
                print("Please select an actual option.")
