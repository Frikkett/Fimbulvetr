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

# Function Definitions

ListA = list(["a",'"a"'," a","a "])
ListB = list(["b",'"b"'," b","b "])
ListC = list(["c",'"c"'," c","c "])
ListD = list(["d",'"d"'," d","d "])
cancel = list(["cancel","stop","back"])
lexit = (["exit", "break", "kill", "die", "leave", " exit", "exit ", "ext", "exi", ])
yes = list(["y","yes","ye","ys","yes "," yes","sure","sur","sre","ure","yeah","yea","yeh","yah","eah","yup","yip","yes please","absolutely","yep"])
no = list(["n","no","nop","nope","not","not really","not realy","no thanks","noo","nooo","noooo","nooooo","never","nno","nnoo"])
ListMenu = list(["menu", "list", "meu", "options", "men", "mnu"])
Items = list([])
itePast = list([])
def printFun(w):
    for char in w:
        time.sleep(0.01)
        print(char, end='')

def repLine(numLine, chaVar):
    global theGame
    write = open(theGame, 'r').readlines()
    wrote = chaVar + "\n"
    write[numLine] = str(wrote)
    writer = open(theGame, 'w')
    writer.writelines(write)
    writer.close()


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
                            makeNew = open(gameDef, "a")
                            makeNew.write("1\n")
                            makeNew.write('Gun\n')
                            makeNew.write('knife\n')
                            makeNew.write('bread\n')
                            makeNew.write('wallet\n')
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
                print("Returning to game...")
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
segCheck = open(theGame,"r")
Navi = str(segCheck.readline().strip())
Navigator =str(Navi)
segCheck.close()
with open(theGame,"r") as segCheck:
    for line in segCheck:
        line = line.strip()
        Items.append(line)
        itePast.append(line)
navPast = str(Navigator)
print(Navigator)
while gameOn == 0:
    if navPast != Navigator:
        Navigatord = str(Navigator)
        repLine(0, Navigatord)
        navPast = str(Navigator)
    if itePast != Items:
        segCheck = open(theGame, "a")
        for i in Items:
            if i not in itePast:
                segCheck.writelines(i)
                itePast.append(i)
        segCheck.close()

    # NOTE TO SELF: DO NOT CHANGE THE BELOW SEGMENT. IT IS THE TEMPLATE FOR COPY AND PASTE.

    if str(Navigator) == "0":
        print('''
        
        ''')
        while True:
            gameChoice = str(input(""))
            if gameChoice.lower() in ListA:
                print('''
            
                ''')
                time.sleep(1)
                Navigator = "1"
                break
            if gameChoice.lower() in ListB:
                print('''
            
                ''')
                time.sleep(1)
                Navigator = "1"
                break
            if gameChoice.lower() in ListC:
                print('''
            
                ''')
                time.sleep(1)
                Navigator = "1"
                break
            if gameChoice.lower() in ListMenu:
                Menu(True)
                break
            else:
                print("Please select an actual option.")

    # NOTE TO SELF: DO NOT CHANGE THE ABOVE SEGMENT. IT IS THE TEMPLATE FOR COPY AND PASTE.

    if str(Navigator) == "1":
        print('''
On October 28th in the year 2020 an immense earthquake rocked the earth. Centered in north america, the quake 
toppled cities and leveled forests. This was not the worst of it, however, as the earthquake set off a catastrophic 
chain of events. Tectonic disturbances caused by the earthquake kick-started a reaction in the Yellowstone volcanic 
caldera, home to the Yellowstone Super-Volcano. Being 2020, of course the volcano erupted. The eruption decimated 
America, and plumes of volcanic ash surrounded the earth.
''')
        input("press [ENTER] to continue")
        print('''
The limited sunlight that pierced the clouds was not enough to properly maintain the earth's climate, 
and the earth plunged into a decades-long winter. Some raving lunatics on the internet compared the current situation to
norse legend of Ragnarok, in which there is a 3 year winter before the end of the world. Thus, the catastrophe
took the name of "Fimbulwinter" 
''')
        input("press [ENTER] to continue")
        print('''
So far, the Fimbulwinter has lasted 26 years. What remains of America is now a hostile, ungoverned land as most of the
wealthy survivors of the eruption fled to Europe and Canada. A new weather event, dubbed "Ashfall", where instead 
of snowflakes volcanic ash falls from the sky, has caused many survivors to huddle together in underground settlements.
The Ashfall is not as bad as it was years ago, but a single breath of the volcanic dust can still lead to severe injury.

''')
        input("press [ENTER] to continue")
        print('''
        
BUT. Where do you fit in? Well, your name is Eliezer Written. You really don't care about all that stuff above, you just 
do what you're told as a part of the Vinter Kin, a growing conglomeration of criminals and idiots. 

You are currently on your way to a small settlement you and your group have decided to ransack, and because of the plot 
it just so happens to be your first raid...
        ''')
        input("press [ENTER] to continue")
        print(''' 


Your jeep skids to a halt as you arrive at the outskirts of the village. Your "Co-workers" leap out, weapons raised, 
and stride towards the defenseless settlement. If they get there, that village will not survive.

        You...
        
        [A] drive away
        
        [B] Walk with them
        
        [C] Mutiny!
        
        (HINT: type the letter in brackets to select the corresponding action)
        ''')
        while True:
            gameChoice = str(input(""))
            if gameChoice.lower() in ListA:
                print(''' 

Alright, coward. 
You turn your back on the innocent village as screams and thunderous gunfire erupt behind you.
Have fun sleeping tonight.


                ''')
                time.sleep(2)
                Navigator = "1A"
                break
            if gameChoice.lower() in ListB:
                print(''' 
                
Really? You actually want to walk straight into a massacre 
WITH the people DOING THE MASSACRING?

                ''')
                time.sleep(1)
                print('''
                
Well, I suppose there's not much I can do to stop you.
You ARE the one making the choices here, so I am legally obligated to let you commit mass murder. 
Just don't expect me to narrate it!

''')
                time.sleep(2)
                Navigator = "1B"
                break
            if gameChoice.lower() in ListC:
                print('''
            
                ''')
                Navigator = "1"
                break
            if gameChoice.lower() in ListMenu:
                Menu(True)
                break
            else:
                print("Please select an actual option.")

    elif str(Navigator) == "1A":
        print('''
So, now that you've abandoned a town of farmers and refugees, what next?
You can't go back to the Vinter Kin, not after THAT display of cowardice.

You could always try to find a home out in the wilderness, although you'd be at risk if there's an ashfall.

Alternatively, you could hit the road and hope you find people before people find you.

        What's it gonna be?
        
        [A] Wilderness
        
        [B] Road
        
        [C] Vinter Kin
        
        
        ''')

        while True:
            gameChoice = str(input(""))
            if gameChoice.lower() in ListA:
                print('''

Okay, but don't blame me if your lungs fill with volcanic cement. I don't write the rules, I just read them.


                ''')
                time.sleep(1)
                Navigator = "1AA"
                break
            if gameChoice.lower() in ListB:
                print('''

Allright! Road trip time!
                ''')
                time.sleep(1)
                Navigator = "1AB"
                break
            if gameChoice.lower() in ListC:
                print('''
            
                ''')
                time.sleep(1)
                Navigator = "1AC"
                break
            if gameChoice.lower() in ListMenu:
                Menu(True)
                break
            else:
                print("Please select an actual option.")
