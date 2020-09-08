# Importing all of the resources required
import os
import time
import random
# a small bit of code to create the save folder if none exist.
saveCheck = os.path.isdir('Fimbulvetr Save File')
if saveCheck == False:
    os.mkdir('Fimbulvetr Save File')

# Global Variables

# inGame - the variable that determines whether or not the user is currently playing the game or just at the starting menu
inGame = False

# theGame - the variable that stores the name of the user-chosen save file.
theGame = str()

# List Definitions

# Error Prevention Lists - These lists contain multiple variations of similar possible inputs. This helps to mitigate any possible
# Input Errors by providing a much wider range of possibilities that all have the same meaning.
ListA = list(["a",'"a"'," a","a "])
ListB = list(["b",'"b"'," b","b "])
ListC = list(["c",'"c"'," c","c "])
ListD = list(["d",'"d"'," d","d "])
cancel = list(["cancel","stop","back"])
lexit = (["exit", "break", "kill", "die", "leave", " exit", "exit ", "ext", "exi", ])
yes = list(["y","yes","ye","ys","yes "," yes","sure","sur","sre","ure","yeah","yea","yeh","yah","eah","yup","yip","yes please","absolutely","yep"])
no = list(["n","no","nop","nope","not","not really","not realy","no thanks","noo","nooo","noooo","nooooo","never","nno","nnoo"])
ListMenu = list(["menu", "list", "meu", "options", "men", "mnu"])

# Item Lists - these lists are used to read and store in-game "items" from the user-chosen save file.
Items = list([])
itePast = list([])

# Death Lists - these provide variation to the possible ways for the player-character to die, making repetitive death-text
# more interesting.

deadBear = list(['''The bear leaps on top of you, crushing your fragile skeleton underneath it's sheer weight. 
The last thing you see before your heart stops is the glistening, drool-coated fangs of the bear presented in a snarl.

You have died.''' , '''The bear stands up, towering over you. With a quick slash of its claws, the bear effortlessly slices your 
major organs.

You have died. ''' , '''The bear charges into you, snapping it's jaws shut around your stomach. You fall backwards and 
slowly lose consciousness.
 
 You have died. '''])

# Function Definitions

# repLine - This function takes two parameters, the number of the desired line and the desired text.
#           The function then clears the desired line and replaces it with the desired text.

def repLine(numLine, changeTxt):
    global theGame
    gameLines = open(theGame, 'r').readlines()
    lineReplace = changeTxt + "\n"
    gameLines[numLine] = str(lineReplace)
    newLines = open(theGame, 'w')
    newLines.writelines(gameLines)
    newLines.close()

# Menu - This function is the ENTIRE game menu, with all of the options and possible uses of the menu. This function
#        allows the user to create, delete, and load files, as well as exit the game or the menu.
#        This function is arguably the most complex part of the entire program.

def Menu(inGame):
    menuStay = 0
    menuUp = 0

    # Defining all required lists and variables as global, so that the function can access them.

    global ListA
    global ListB
    global ListC
    global ListD
    global theGame
    global yes
    global no
    global lexit
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
            # loadLoop determines whether the load option loops or not
            loadLoop = 0
            # deadLoop determines whether the delete option loops or not
            deadLoop = 0
            menuChoice = str(input('''
==='''))
            if menuChoice.lower() in ListA:
                # Opens the directory 'Fimbulvetr Save File'
                optionsCheck = os.listdir('Fimbulvetr Save File')
                # counts the number of files in the directory
                optionsNum = len(optionsCheck)
                if optionsNum == 0:
                    # Returns a message if there are no files
                    print("I'm sorry, it appears that there are no save files on this computer.")
                else:
                    # Returns the number of files in the directory, and prints the names of the files for the user to see
                    print("There are {} saved files on this computer. they are:".format(optionsNum))
                    print(optionsCheck)
                    print('''
Please enter the name of the file you would like to load, or type "cancel" to cancel loading.''')
                    while loadLoop == 0:
                        loadName = str(input("==="))
                        loadTxt = loadName + ".txt"
                        # checks to see if the user's input is a valid file option
                        if loadName in optionsCheck:
                            while True:
                                # asks for the user's confirmation
                                print("Are you sure you want to load {}?".format(loadName))
                                loadSure = input("Yes/No:")
                                if loadSure.lower() in yes:
                                    print('''
Loading {}.'''.format(loadName))
                                    # Sets the value of theGame and breaks all function loops.
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
                            # checks to see if the user's input with .txt at the end is a valid file option
                            while True:
                                # asks for the user's confirmation
                                print("Are you sure you want to load {}?".format(loadTxt))
                                loadSure = input("Yes/No:")
                                if loadSure.lower() in yes:
                                    print('''
Loading {}.'''.format(loadTxt))
                                    # Sets the value of theGame and breaks all function loops.
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
                    # Asks the user for a name for their save file
                    print("What would you like to call your game? (type 'Cancel' to exit)")
                    gameName = str(input())
                    gameDef = "Fimbulvetr Save File/" + gameName + ".txt"
                    try:
                        if gameName in cancel:
                            print("Cancelled.")
                            makeTry = False
                        else:
                            # Fills the new file with all of the basic essentials
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
                # Opens the directory 'Fimbulvetr Save File'
                optionsCheck = os.listdir('Fimbulvetr Save File')
                # counts the number of files in the directory
                optionsNum = len(optionsCheck)
                if optionsNum == 0:
                    # Returns a message if there are no files
                    print("I'm sorry, it appears that there are no save files on this computer.")
                else:
                    # Returns the number of files in the directory, and prints the names of the files for the user to see
                    print("There are {} saved files on this computer. they are:".format(optionsNum))
                    print(optionsCheck)
                    print('''
Please enter the name of the file you would like to EXTERMINATE, or type "cancel" to cancel EXTERMINATION.''')
                    while deadLoop == 0:
                        deadName = str(input("==="))
                        deadTxt = deadName + ".txt"
                        # checks to see if the user's input is a valid file option
                        if deadName in optionsCheck:
                            while True:
                                # checks for the user's confirmation
                                print("Are you ABSOLUTELY SURE you want to EXTERMINATE {}?".format(deadName))
                                deadSure = input("Yes/No:")
                                if deadSure.lower() in yes:
                                    print('''
Exterminate!''')
                                    time.sleep(0.2)
                                    print('''
Ex-ter-min-ate!!''')
                                    time.sleep(0.2)
                                    print('''
...''')
                                    time.sleep(0.2)
                                    print('''
{} Exterminated.'''.format(deadName))
                                    deleteName = "Fimbulvetr Save File/" + deadName
                                    # Deletes the save file.
                                    os.remove(deleteName)
                                    deadLoop = 1
                                    break
                                elif deadSure.lower() in no:
                                    print("EXTERMINATION Cancelled")
                                    deadLoop = 1
                                    break
                        elif deadTxt in optionsCheck:
                            # checks to see if the user's input with .txt at the end is a valid file option
                            while True:
                                # asks for the user's confirmation
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
                                    # Deletes the save file.
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
                # Returns to game
                menuUp = 1
                menuStay = 1
            elif menuChoice.lower() in lexit:
                print("Exiting Program.")
                # Exits the program
                exit()
            else:
                print("Type an actual option please.")


# MainGame Loop
# opens the start menu
Menu(False)
gameOn = 0
segCheck = open(theGame,"r")
Navi = str(segCheck.readline().strip())
Navigator = str(Navi)
segCheck.close()

with open(theGame,"r") as segCheck:
    for line in segCheck:
        line = line.strip()
        Items.append(line)
        itePast.append(line)

navPast = str(Navigator)
print(" Hint: You can type 'Menu' into any typing prompt during the game to open the menu.")
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
                input("press [ENTER] to continue")
                Navigator = "1"
                break
            if gameChoice.lower() in ListB:
                print('''
            
                ''')
                input("press [ENTER] to continue")
                Navigator = "1"
                break
            if gameChoice.lower() in ListC:
                print('''
            
                ''')
                input("press [ENTER] to continue")
                Navigator = "1"
                break
            if gameChoice.lower() in ListMenu:
                Menu(True)
                break
            else:
                print("Please select an actual option.")

    # NOTE TO SELF: DO NOT CHANGE THE ABOVE SEGMENT. IT IS THE TEMPLATE FOR COPY AND PASTE.
    # NOTE TO SELF: DO NOT CHANGE THE BELOW SEGMENT. IT IS THE TEMPLATE FOR DEATH.

    if str(Navigator) == "XY":
        deadNum = random.randint(0, 5)
        print(dead___(deadNum))
        gameOn = 1

    # NOTE TO SELF: DO NOT CHANGE THE ABOVE SEGMENT. IT IS THE TEMPLATE FOR DEATH.

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
                input("press [ENTER] to continue")
                Navigator = "1A"
                break
            if gameChoice.lower() in ListB:
                print(''' 
                
Really? You actually want to walk straight into a massacre 
WITH the people DOING THE MASSACRING?

                ''')
                input("press [ENTER] to continue")
                print('''
                
Well, I suppose there's not much I can do to stop you.
You ARE the one making the choices here, so I am legally obligated to let you commit mass murder. 
Just don't expect me to narrate it!

''')
                input("press [ENTER] to continue")
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
                input("press [ENTER] to continue")
                Navigator = "1AA"
                break
            if gameChoice.lower() in ListB:
                print('''

Alright! Road trip time!



                ''')
                input("press [ENTER] to continue")
                Navigator = "1AB"
                break
            if gameChoice.lower() in ListC:
                print('''

So you remember how, not five minutes ago, you abandoned and betrayed members of the very group you now want to return
to? Just figured I'd mention that.



                ''')
                input("press [ENTER] to continue")
                Navigator = "1AC"
                break
            if gameChoice.lower() in ListMenu:
                Menu(True)
                break
            else:
                print("Please select an actual option.")

    elif str(Navigator) == "1AB":
        print('''
You drive along the narrow abandoned street, listening to your music at full volume when you come to an old piece of
cracked, mostly obliterated road.

There are no signs telling you where your options lie
        ''')
        input("press [ENTER] to continue")
        print('''
To your left lies a mostly overgrown, partly dirt road that looks like it could lead to something.
There is an almost untouched street to your right, with trimmed bushes, and beautiful houses.
The road to your front is.... well.... kinda half gone.

Not like covered or anything.

More like fell from a landslide.

        So, where do you go?
        
        [A] Left
        
        [B] Forward
        
        [C] Right
        
        
        
        ''')
        while True:
            gameChoice = str(input(""))
            if gameChoice.lower() in ListA:
                print('''
Left... Ok then, it's your funeral.
                ''')
                input("press [ENTER] to continue")
                Navigator = "1ABA"
                break
            if gameChoice.lower() in ListB:
                print('''
            
                ''')
                input("press [ENTER] to continue")
                Navigator = "1ABB"
                break
            if gameChoice.lower() in ListC:
                print('''
            
                ''')
                input("press [ENTER] to continue")
                Navigator = "1ABC"
                break
            if gameChoice.lower() in ListMenu:
                Menu(True)
                break
            else:
                print("Please select an actual option.")

    elif str(Navigator) == "1ABA":
        print('''
You drive along the track to what looks like an abandoned scrapyard. There are old cars, trucks and even a couple of
classic motorcycles to your disappointment.
                ''')
        input("press [ENTER] to continue")
        print('''
Your jeep is looking a bit.. battered, if I must say.

And in complete honesty, I'm surprised its still running...

        What's the plan?
        
        [A] Go into the scrapyard in search of a new ride
        
        [B] Salvage the vehicles there to repair your jeep
        
        [C] Summon a 4.8L supercharged DOHC V8 engine to replace your current engine
                ''')
        while True:
            gameChoice = str(input(""))
            if gameChoice.lower() in ListA:
                print('''

                ''')
                input("press [ENTER] to continue")
                Navigator = "1ABAA"
                break
            if gameChoice.lower() in ListB:
                print('''

                ''')
                input("press [ENTER] to continue")
                Navigator = "1ABAB"
                break
            if gameChoice.lower() in ListC:
                print('''

                ''')
                input("press [ENTER] to continue")
                Navigator = "1ABAC"
                break
            if gameChoice.lower() in ListMenu:
                Menu(True)
                break
            else:
                print("Please select an actual option.")

    elif str(Navigator) == "1ABAA":
        print('''
        !!!!!!!!!!!!!!!!!!!!!!!!!!!DIE!!!!!!!!!!!!!!!!!!!!!!!!!!!
        ''')
        while True:
            gameChoice = str(input(""))
            if gameChoice.lower() in ListA:
                print('''
            
                ''')
                input("press [ENTER] to continue")
                Navigator = "1"
                break
            if gameChoice.lower() in ListB:
                print('''
            
                ''')
                input("press [ENTER] to continue")
                Navigator = "1"
                break
            if gameChoice.lower() in ListC:
                print('''
            
                ''')
                input("press [ENTER] to continue")
                Navigator = "1"
                break
            if gameChoice.lower() in ListMenu:
                Menu(True)
                break
            else:
                print("Please select an actual option.")
                

    elif str(Navigator) == "1AA":
        print('''
You continue driving, constantly on the look-out for anywhere that could provide enough shelter, like a cave or a 
particularly dense cluster of trees. 

After driving about 30 kilometers (Yes, I'm using the metric system. I'm not a monster.) northwest of that one town 
where I lost all respect for you, a slight clearing in the trees to your left catches your attention. It seems to 
be some sort of trail.

        Pulling the jeep closer, you...
        
        [A] Hide the jeep and walk down the trail
        
        [B] Investigate the trail
        
        [C] Drive down the trail
        
        
        ''')
        while True:
            gameChoice = str(input(""))
            if gameChoice.lower() in ListA:
                print('''

Parking the jeep in a cluster of bushes, You take a bit of time covering the vehicle with branches and leaves until 
you're... mildly confident with the make-shift camouflage. Looking over your handiwork once more, you set off down the
trail.



                ''')
                input("press [ENTER] to continue")
                Navigator = "1AAA"
                break
            if gameChoice.lower() in ListB:
                print('''

"Before I just charge in," you rationalize, "I should probably make sure the path is safe."

Taking a moment to investigate the path, you almost immediately spot the huge, muddy paw-prints of a bear. Knowing that 
you'd be at a major disadvantage if you attempted to fight a bear in such a dense forest, you decide to look somewhere else. 


 
                ''')
                input("press [ENTER] to continue")
                Navigator = "1AAB"
                break
            if gameChoice.lower() in ListC:
                print('''

It's a tight fit, but you manage to get the jeep onto the trail. After about 10 minutes of driving, a spine-chilling 
grind of metal on stone reverberates throughout the forest, and you realise you've hit a rock.


                ''')
                input("press [ENTER] to continue")
                Navigator = "1AAC"
                break
            if gameChoice.lower() in ListMenu:
                Menu(True)
                break
            else:
                print("Please select an actual option.")

    elif str(Navigator) == "1AAA":
        print('''
        
You hike up the trail for a while, probably about 40 minutes, and you're starting to like your surroundings. 
You're in a wide valley, nice trees, beautiful sky, you even passed a river so there's plenty of water.

A crack in the bushes to your right startles you, and you spin around to see a brown bear twice your size.

        You...
        
        [A] Run!
        
        [B] Punch it's snout into the stratosphere
        ''')
        c = False
        if "Gun" in Items:
            print('''
        [C] Do what any sensible American man would do. Git yer gun.
        
        ''')
            c = True
        while True:
            gameChoice = str(input(""))
            if gameChoice.lower() in ListA:
                print('''
            
You immediately whip around and bolt down the trail, trying to put as much distance between you and the bear. Such an 
attempt is futile, however, as the bear is gaining on you. You turn a corner and find yourself at a dead end.

Remember that village you doomed? Well now you're just as helpless as them.
It's Karma time.
                ''')
                input("press [ENTER] to continue")
                Navigator = "FB"
                break
            if gameChoice.lower() in ListB:
                print('''

Oh okay, I get it. You thought that this option was a joke, or that I was exaggerating when I said "stratosphere."

I wasn't. 

With the might of a hundred ridiculously overpowered protagonists, you whapp the bear on the nose so forcefully that
it causes the laws of physics to do a double take and the bear rockets into the sky like a fluffy meteorite in reverse.

                ''')
                input("press [ENTER] to continue")
                Navigator = "1AAAB"
                break
            if c is True and gameChoice.lower() in ListC:
                print('''
        
Looks like we got ourselves a good 'Ol canadian stand off.


                ''')
                input("press [ENTER] to continue")
                Navigator = "1AAAC"
                break
            if gameChoice.lower() in ListMenu:
                Menu(True)
                break
            else:
                print("Please select an actual option.")

    elif str(Navigator) == "1AAAB":
        print('''
        
So, now that you've enlisted Americas first ever Astro-Bear, you continue down the road. You continue the hike for a 
good 4 kilometres, until you finally arrive at an imposing iron gate, complete with plenty of barbs and pointy bits.

Beyond the gate, It looks like there's an abandoned house of some kind.

        You...
        
        [A] Use your overwhelming, bear-a-pulting strength to wrench apart the bars
        
        [B] climb up a tree and leap over the gate
        ''')
        while True:
            gameChoice = str(input(""))
            if gameChoice.lower() in ListA:
                print('''

This is it. You've trained your whole today for this moment. You plunge your hands into the gap between two bars and, 
screaming loud enough to make a boeing 747 file a noise complaint, you widen the gap enough to just bear-ly squeeze through. 
On the other side, sweating enough to flood a small town, (with water rather than bullets, this time.) you lean on the
gate.

As you put your full weight on the gate, It swings open.
''')
                input("press [ENTER] to continue")
                print('''

Honestly I have no clue why you didn't just open the gate, after all it was never locked.


                ''')
                input("press [ENTER] to continue")
                Navigator = "1AAABA"
                break
            if gameChoice.lower() in ListB:
                print('''

You know what they say, the brain's like a muscle. Considering your impossible muscles, you must have a pretty big brain.

                ''')
                input("press [ENTER] to continue")
                print('''
I'm just disappointed that THIS was the best plan you could come up with.
                ''')
                input("press [ENTER] to continue")
                Navigator = "1AAABB"
                break
            if gameChoice.lower() in ListMenu:
                Menu(True)
                break
            else:
                print("Please select an actual option.")

    elif str(Navigator) == "1AAABA":
        print('''
        
As you walk towards the house, the sky turns grey-er, and you pick up the pace. By the time you reach the front door, 
you had begun sprinting. 

Just in time, too, as the first specks of the Ashfall were just touching the ground. A rusted plaque on the door 
reads: "Bear House"

Pushing on the door, you find that it too is unlocked.

To your surprise, however, it is NOT abandoned. 
        ''')
        input("press [ENTER] to continue")
        print('''
Not by bears, anyway.
''')
        input("press [ENTER] to continue")
        print('''
        
Two more brown bears are sitting at a table, eating what looks to be porridge. One of them is roughly the same size 
as the previous bear, although it's fur is a few shades darker. The other bear appears to be a cub of some kind.

        You...
        
        [A] Properly operate these punching bags
        
        [B] Growl
        
        [C] sit down and eat with them 
        
        ''')
        while True:
            gameChoice = str(input(""))
            if gameChoice.lower() in ListA:
                print('''

Looks like Papa Bear was just a warm up!

Cracking your knuckles, you shift into an offensive stance. With a bar-bear-ic gleam in your eyes, you charge at Mama
Bear and throw a punch, which she effortlessly catches.
                ''')
                input("press [ENTER] to continue")
                print('''

Mama Bear rises from her chair to tower over you.

"So," she whispers, "I take it YOU'RE the one who defeated MY Ro-bear-to?"

"And what if I did?" you reply.

''')
                input("press [ENTER] to continue")
                print('''
She snarls and, grabbing you by the arm, swings you into the air and back down again like a certain green rage monster
I can't name because copyright.

You leap on to your feet and twist out of her grip, only to receive a sharp blow to the head. Mama Bear follows up with
a series of quick strikes to the head and lower torso, although you manage to dodge more than a few of her attacks. 
                ''')
                input("press [ENTER] to continue")
                print('''
"Have you figured it out yet?" Mama Bear growls, "I'm no ordinary bear. I've been trained in the ancient ways of 
Bear-zilian Griz-jitsu, You stand no chance!"

As a response to her claim you charge into her like a bull, tackling her through the nearest wall.
                ''')
                input("press [ENTER] to continue")
                print('''
You continue charging forwards, crashing through trees and walls. Mama Bear plants her feet, grabs onto your sides, 
and lifts you over her head.

"THIS, is for my wallpaper," Mama Bear hisses as she slams your spine into her knee, "THIS, is for my trees," she snaps as
she rolls you into a ball and chucks your aching body high into the air. 

"And THIS," Mama Bear shouts, her voice frothing with rage, as she leaps up to meet you, "IS FOR ROBEARTO!!!"
Mama Bear proceeds to volleyball slap you straight into the nearest mountain, which happens to be right behind the Bear
House.
          ''')
                input("press [ENTER] to continue")
                Navigator = "1AAABAA"
                break
            if gameChoice.lower() in ListB:
                print('''
You bare your teeth and growl.

The larger bear, who you soon learn is Mama Bear Bear-a-trice, growls back.

You growl again. Bearatrice growls back, but with an edge of interest. You growl about your day. Bearatrice growls 
about hers. The cub, Bear-naby, growls about the eccentric intricacies in the local woodland politics. You growl
out a joke about honeybees, causing all of you to laugh. You follow it up with a joke you've been working on all day,
about that bear you sent flying. 

It takes three whole seconds of silence for you to realise your mistake.

You hurriedly try to growl out an apology, but Bearatrice isn't having any of it. She stands up.
                ''')
                input("press [ENTER] to continue")
                Navigator = "FB"
                break
            if gameChoice.lower() in ListC:
                print('''
You hang up your coat on a nearby rack, sit down at the table, and grab an unclaimed bowl of porridge.
Mama bear and cub bear abruptly stop eating to stare directly at you, both of them looking more confused than an airplane pilot
who just received a parking violation mid-flight.

The two bears glance at one another, nod, and lunge across the table at you.
                ''')
                input("press [ENTER] to continue")
                print('''
Did you SERIOUSLY expect that to work?
''')
                input("press [ENTER] to continue")
                Navigator = "FB"
                break
            if gameChoice.lower() in ListMenu:
                Menu(True)
                break
            else:
                print("Please select an actual option.")

    elif str(Navigator) == "1AAABAA":
        print('''

Pulling yourself up from the rubble of the small crater you made in the mountain, you can make out Mama Bear bounding
across the valley towards you at an alarming speed.

        You...
        
        [A] Hurl the rocky rubble at Mama Bear! 
        
        [B] Call upon your ungodly Bar-bear-ian prowess
        
        [C] Laser Eyes!
                ''')
        while True:
            gameChoice = str(input(""))
            if gameChoice.lower() in ListA:
                print('''
You stare directly at the rubble, imagining it as lumpy, petrified bears. You heft two boulders, each twice your size, 
and hurl them towards Mama Bear.
                ''')
                input("press [ENTER] to continue")
                print('''
Mama Bear charges straight through the first boulder, shattering it. Granite chunks and debris spray out behind her as
she continues her murderous rampage. The second boulder flies at her fast, but Mama Bear just leaps onto it, using it
like a spring board to propel towards you.
                ''')
                Navigator = "1"
                break
            if gameChoice.lower() in ListB:
                print('''
            
                ''')
                input("press [ENTER] to continue")
                Navigator = "1"
                break
            if gameChoice.lower() in ListC:
                print('''
            
                ''')
                input("press [ENTER] to continue")
                Navigator = "1"
                break
            if gameChoice.lower() in ListMenu:
                Menu(True)
                break
            else:
                print("Please select an actual option.")



    elif str(Navigator) == "FB":
        deadNum = random.randint(0, 2)
        print(deadBear[deadNum])
        gameOn = 1
