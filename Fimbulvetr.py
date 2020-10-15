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

deadDog = list(['''The dogs pounce on you and tear apart your flesh with their jaws. Your last sight is seeing one of the dogs
chomping down on your face...

You have died.''' , '''The dogs surround you. There's no chance you'll survive despite your (non-existent) survival
skills. They eventually overpower you when their owner walks over to you with his gun loaded.

*BANG!*

You have died.''' , '''You decide to ride away from the dogs. The motorcycle is fast, and you lose control quickly, sending
you directly into a powerpole. The voltage running through the pole is redirected into the fuel tank of your motorcycle,
and the resulting fireball incinerates your already mutilated body.

You have died'''])

deadFlame = list(['''You are instantly burned to a crisp and melt away into dust.
	
You have died.''' , '''You inhale the flames and have your organs fried like potato chips.
	
You have died.''' , '''You let the flames consume you as you ponder your life, your childhood, everything in your past,	
when you let out your last breath with a sigh of relief, knowing that you died in a really stupid way.
	
You have died.''' , '''The flames begin to burn, slowly melting your body down. Then you somehow melt like	
an ice cream. That was weird.
	
You have died.'''])

deadDrown = list(['''Your inability to swim becomes your downfall as you slowly stumble deeper into the water.

You have died.''' , '''The pure joy of being in water for the first time in your life unfortunately ends it, as your
excitement creates so much heat it fries your brain before you can think twice.

You have died.''' , '''The toxins in the water from years of pollution and ashfall comsume you as you splash around without
knowledge that your body is quickly decaying.

You have died.'''])
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
    # This "While" loop allows me to end the "Menu" function when the independent variable "menuUp" is altered.
    while menuUp == 0:
        # the "r" before the three quote marks allows me to display the Text art below. Usually, the back-slashes-"\"-would signal the program to
        # print some kind of whitespace in their place (\t = tab, \n = newline, etc.). The "r", however, prevents this by telling the program to ignore
        # the backslash formatting and instead just print the text as it is.
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
        # presents the user with options
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
            # Gives the user an additional option if the user is currently playing the game.
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
            # This section of the function deals with loading pre-existing save files.
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
                                    # cancels the load if the user is unsure.
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
                                    # cancels the load if the user is unsure.
                                    print("Load Cancelled")
                                    loadLoop = 1
                                    break
                        elif loadName.lower() in cancel:
                            # cancels the load if the user tells the program to.
                            print("Load Cancelled")
                            break
                        else:
                            # returns a message if the user enters an invalid input.
                            print("Please type an actual option from the list.")

            # This section of the function deals with creating new save files.
            elif menuChoice.lower() in ListB:
                # This "While" loop allows me to end the "New Game" section of the function when the independent variable "makeTry" is altered.
                # It also allows the user to continue trying to make new game files if they happen to enter an invalid input.
                makeTry = True
                while makeTry == True:
                    # Asks the user for a name for their save file
                    print("What would you like to call your game? (type 'Cancel' to exit)")
                    gameName = str(input())
                    # Sets the variable "gameDef" to the correct format for opening files.
                    gameDef = "Fimbulvetr Save File/" + gameName + ".txt"
                    try:
                        if gameName in cancel:
                            # cancels the "New Game" section of the function if the user enters an input that is in the "cancel" list.
                            print("Cancelled.")
                            makeTry = False
                        else:
                            # Fills the new file with all of the basic essentials
                            makeNew = open(gameDef, "x")
                            makeNew.close()
                            makeNew = open(gameDef, "a")
                            makeNew.write("1\n")
                            makeNew.write('knife\n')
                            makeNew.write('bread\n')
                            makeNew.write('wallet\n')
                            makeNew.close()
                            # Tells the user the name of their game and it's location in the computer's files.
                            print("Your game is called {}.".format(gameName))
                            print("Your game is located at {}.".format(gameDef))
                            print('''
Please Enjoy the game.''')
                            theGame = gameDef
                            menuUp = 1
                            menuStay = 1
                            makeTry = False
                    except FileExistsError:
                        # detects when the entered name is already in use and informs the user.
                        print("This name is already in use. Please choose a different name.")

            # This section of the function deals with Deleting pre-existing save files.
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
                                    # Cancels deletion if the user is unsure
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
                                    # Cancels deletion if the user is unsure
                                    print("EXTERMINATION Cancelled")
                                    deadLoop = 1
                                    break
                        elif deadName.lower() in cancel:
                            # cancels the "Delete" section of the function if the user enters an input that is in the "cancel" list.
                            print("EXTERMINATION Cancelled")
                            break
                        else:
                            print("Please type an actual option from the list.")
            elif menuChoice.lower() in ListD:
                if inGame == True:
                    print("Returning to game...")
                    # Returns to game
                    menuUp = 1
                    menuStay = 1
                else:
                    print("Type an actual option please.")
            elif menuChoice.lower() in lexit:
                print("Exiting Program.")
                time.sleep(2)
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
    # NOTE TO SELF: DO NOT CHANGE THE BELOW SEGMENT. IT IS THE TEMPLATE FOR ENDINGS.

    if str(Navigator) == "XY":
        deadNum = random.randint(0, 5)
        print(dead___(deadNum))
        gameOn = 1

    # NOTE TO SELF: DO NOT CHANGE THE ABOVE SEGMENT. IT IS THE TEMPLATE FOR ENDINGS.

    # From here, the majority of the program is repetition of the same altered segment.

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
                print(" SORRY, BUT THIS PATH HAS BEEN DEMOLISHED BY A FLAMING BEAR. PLEASE CHOOSE A DIFFERENT OPTION")
                break
            if gameChoice.lower() in ListC:
                print('''
            
                ''')
                print(" SORRY, BUT THIS PATH HAS BEEN DEMOLISHED BY A FLAMING BEAR. PLEASE CHOOSE A DIFFERENT OPTION")
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
                print(" SORRY, BUT THIS PATH HAS BEEN DEMOLISHED BY A FLAMING BEAR. PLEASE CHOOSE A DIFFERENT OPTION")
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
The road to your front is half gone.

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
                print(" SORRY, BUT THIS PATH HAS BEEN DEMOLISHED BY A FLAMING BEAR. PLEASE CHOOSE A DIFFERENT OPTION")
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

And in complete honesty, I'm surprised it's still running...

        What's the plan?
        
        [A] Go into the scrapyard in search of a new ride
        
        [B] Salvage the vehicles there to repair your jeep
        
        [C] Summon a 4.8L supercharged DOHC V8 engine to replace your current engine
                ''')
        while True:
            gameChoice = str(input(""))
            if gameChoice.lower() in ListA:
                print('''
Nice, time for a new ride. Can't say it'll be amazing, but it'll be something.


                ''')
                input("press [ENTER] to continue")
                print('''
You waddle around the various vehicles and parts, examining them in their non-existent glory. There is a bright red
motorcycle that catches your eye, with its massive blastpipes and lack of muffler, it's perfect.

Just keep the volume down. There are dogs sleeping nearby that look sorta dangerous...
                ''')
                input("press [ENTER] to continue")
                print('''
You sit down on the seat, and to your joy, the keys are in. You turn the key, and it roars to life with massive pink
flames roaring out the pipes...

Pink? What...

Then the stereo starts playing children's music at full volume

Why does it have a stereo? That's weird, but either way, now there's a bunch of dogs you've woken up that are rushing
to eat you. I hope you feel stupid.
                ''')
                input("press [ENTER] to continue")
                Navigator = "FD"
                break
            if gameChoice.lower() in ListB:
                print('''

                ''')
                input("press [ENTER] to continue")
                print(" SORRY, BUT THIS PATH HAS BEEN DEMOLISHED BY A FLAMING BEAR. PLEASE CHOOSE A DIFFERENT OPTION")
                break
            if gameChoice.lower() in ListC:
                print('''

                ''')
                input("press [ENTER] to continue")
                print(" SORRY, BUT THIS PATH HAS BEEN DEMOLISHED BY A FLAMING BEAR. PLEASE CHOOSE A DIFFERENT OPTION")
                break
            if gameChoice.lower() in ListMenu:
                Menu(True)
                break
            else:
                print("Please select an actual option.")

    elif str(Navigator) == "1ABB":
        print('''
You aren't very certain that even if you drive safely over this semi consumed road you'll make it over, so you step on
it. The jeep somehow accelerates to its top speed of 450km/h in the space of a couple metres. How the G-forces didn't
shred you, I have no clue.
        ''')
        input("press [ENTER] to continue")
        print('''
You drive straight over the gaps in the road at stupidly high speeds when the road ends.

It just ends.

You hit a solid barrier at speed and get sent out the front window. You dolphin dive a few km, passing a nearby plane at
a great altitude
        ''')
        input("press [ENTER] to continue")
        print('''	
As you pass the biplane, you manage to see the pilot, smoking a pipe, as you fly through the atmosphere.	
"Oh Hi" you say	
"Hello there," the pilot responds, "It's dangerous to go alone. Take this."	
He hands you a gun for some reason. Could be useful.	
        ''')
        Items.append("Gun")
        input("press [ENTER] to continue")
        print('''	
You get a good view of the surrounding area. Do you...	
    [A] Land in a forest	
    	
    [B] Steal the plane	
    	
    [C] Wing it
    ''')
        while True:
            gameChoice = str(input(""))
            if gameChoice.lower() in ListA:
                print('''
You land in the forest with a slight squeak...
                ''')
                input("press [ENTER] to continue")
                Navigator = "1AAA"
                break
            if gameChoice.lower() in ListB:
                print('''
You decide to point your newly gained gun at the pilot...	 
           
He pulls out a flamethrower.           
                ''')
                input("press [ENTER] to continue")
                print('''
He fires the flamethrower directly at you, lightly toasting every inch of your body in the process.	
                ''')
                Navigator = "FF"
                break
            if gameChoice.lower() in ListC:
                print('''
You flap your arms faster than a humming bird and begin to accelerate past the plane.
                ''')
                input("press [ENTER] to continue")
                Navigator = "FP"
                break
            if gameChoice.lower() in ListMenu:
                Menu(True)
                break
            else:
                print("Please select an actual option.")


    elif str(Navigator) == "1ABAB":
        print('''
You find various pieces of scrap metal to repair your jeep, and over the course of a couple of minutes you make your
once battered unit of a car into a pristine luxury off road vehicle. How did that take a few minutes exactly?

That doesn't matter though, because there is an ashfall coming.
        ''')
        input("press [ENTER] to continue")
        print('''
Do you...

    [A] Drive down the trail to avoid the ashfall
    
    [B] Trust in your newly constructed car
    
    [C] Have a picnic
        ''')
        while True:
            gameChoice = str(input(""))
            if gameChoice.lower() in ListA:
                print('''
That's probably a smart idea, but I thought you didn't care about this sorta stuff...
                ''')
                input("press [ENTER] to continue")
                Navigator = "1ABABA"
                break
            if gameChoice.lower() in ListB:
                print('''
Yes, because your homemade luxury jeep definitely would pass the road fitness test.
                ''')
                input("press [ENTER] to continue")
                Navigator = "FRA"
                break
            if gameChoice.lower() in ListC:
                print('''
Oh what a wonderful idea.
                ''')
                input("press [ENTER] to continue")
                Navigator = "1ABABC"
                break
            if gameChoice.lower() in ListMenu:
                Menu(True)
                break
            else:
                print("Please select an actual option.")

    elif str(Navigator) == "1ABABA":
        print('''
You drive away from the ashfall without issues in the most beautiful weather you've ever seen, which is cloudy.
        ''')
        input("press [ENTER] to continue")
        print('''
You drive for hours on end until you reach what looks like a beach. Honestly, how'd you find one of those?

Do you...

    [A] Have a swim
    
    [B] Sit on the beach eating a sandwich
    
    [C] Also have a swim, but the water is warmer than normal
        ''')
        while True:
            gameChoice = str(input(""))
            if gameChoice.lower() in ListA:
                print('''
Well, this will be exciting.

You run into the water and 'swim' further into the water.
                ''')
                input("press [ENTER] to continue")
                Navigator = "FDW"
                break
            if gameChoice.lower() in ListB:
                print('''
Yum! Banana, mayo and olive sandwiches. My favourite! (Not really)
                ''')
                input("press [ENTER] to continue")
                Navigator = "1ABABAB"
                break
            if gameChoice.lower() in ListC:
                print('''
The ocean has decided to become a giant spa pool.

You decide that leaping into the middle of the ocean is a smart idea, so you do just that.

You land directly in the middle of the ocean.
                ''')
                input("press [ENTER] to continue")
                Navigator = "FDW"
                break
            if gameChoice.lower() in ListMenu:
                Menu(True)
                break
            else:
                print("Please select an actual option.")

    elif str(Navigator) == "FRA":
        print('''
Your luxury jeep was made for luxury, not practicality.

You sit inside your jeep when the ashfall pours down on the roof, eventualy creating too much weight on your car,
sending metal and cloth and electrical wiring down onto you, crushing your skeleton and ending your measly life quickly.

You have died.
        ''')
    elif str(Navigator) == "1ABABC":
        print('''
Your picnic consists of many different foods and drinks. Its a shame you don't have anyone to share it with...
        ''')
        input("press [ENTER] to continue")
        print('''
To your surprise, a glowing yellow van full of crackheads rolls up to your picnic and sit down with you. They ask if
they can join you on your picnic. There's plenty to go around.

Do you...

    [A] Say yes to these pipesmokers
    
    [B] Eat all the food yourself
    
    [C] Activate self defence mode
        ''')
        while True:
            gameChoice = str(input(""))
            if gameChoice.lower() in ListA:
                print('''
Ok then, looks like you've somehow got some friends.
                ''')
                input("press [ENTER] to continue")
                Navigator = "FHP"
                break
            if gameChoice.lower() in ListB:
                print('''
Wow, you greedy glutton. I've never seen someone be so selfish.

Actually I have, but that was also you.
                ''')
                input("press [ENTER] to continue")
                Navigator = "FFF"
                break
            if gameChoice.lower() in ListC:
                print('''
Activating self defence mode...

Why do you have a self defence mode?
                ''')
                input("press [ENTER] to continue")
                Navigator = "FSDM"
                break
            if gameChoice.lower() in ListMenu:
                Menu(True)
                break
            else:
                print("Please select an actual option.")

    elif str(Navigator) == "1ABABAB":
        print('''
You chop down on your war-crime of a sandwich with the most disgusted smile I've seen since your parents had you.

Do you eat more though?

    [A] Yes
    
    [B] No. Get rid of it.
        ''')
        while True:
            gameChoice = str(input(""))
            if gameChoice.lower() in ListA:
                print('''
So you want the rest?

What the hell is wrong with you?
                ''')
                input("press [ENTER] to continue")
                Navigator = "FFS"
                break
            if gameChoice.lower() in ListB:
                print('''
Good choice. Seriously, good choice.
                ''')
                input("press [ENTER] to continue")
                Navigator = "FHE"
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
                Navigator = "1AB"
                break
            if gameChoice.lower() in ListC:
                print('''

It's a tight fit, but you manage to get the jeep onto the trail. After about 10 minutes of driving, a spine-chilling 
grind of metal on stone reverberates throughout the forest, and you realise you've hit a rock.


                ''')
                input("press [ENTER] to continue")
                print(" SORRY, BUT THIS PATH HAS BEEN DEMOLISHED BY A FLAMING BEAR. PLEASE CHOOSE A DIFFERENT OPTION")
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
                print(" SORRY, BUT THIS PATH HAS BEEN DEMOLISHED BY A FLAMING BEAR. PLEASE CHOOSE A DIFFERENT OPTION")
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
                
The tree is pretty high up, although you could probably make it. You leap onto the tree and climb up to a good 
overhanging branch. From this branch, you can see over the house into the valley. Taking a moment to gaze into the sky, 
both suns bright and burning, you leap off the branch.

                ''')
                input("press [ENTER] to continue")
                print('''
                
Soaring through the air, you realise there aren't two suns. Twisting around mid leap, you see a flaming bear plummeting 
straight towards you.
                ''')
                Navigator = "FMB"
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
        
        [B] Show these puny bears who's in charge!
        
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
                input("press [ENTER] to continue")
                print('''
You brace for impact as Mama Bear crashes into you, pushing you back a solid 5 meters. Mama Bear rears back to slash, 
but you interrupt her with a cringe-inducing punch to the gut. The impact of your strike echos through the valley, and 
Mama Bear doubles over in agony.
                ''')
                input("press [ENTER] to continue")
                Navigator = "1AAABAAA"
                break
            if gameChoice.lower() in ListB:
                print('''
You bear your teeth and snarl. Who does this bear think she is? How could she have the AUDACITY to fight a mighty, 
over-bear-ing lord such as yourself? You leap straight at Mama Bear in a blind fury, the only thing you care about
right now is disposing of the problem in front of you.
                ''')
                input("press [ENTER] to continue")
                print('''
Unfortunately, you don't notice the problem BEHIND you.
                ''')
                input("press [ENTER] to continue")
                print('''
The Cub bear soars out of the Bear House at lightning fast speeds, biting into the back of your neck. This catches 
you off guard, and in your brief moment of hesitation, Mama bear lunges in with a lethal swipe to the chest.
                ''')
                Navigator = "FCB"
                break
            if gameChoice.lower() in ListC:
                print('''
Well, if you can punt a bear to the moon then who's to say you CAN'T shoot lasers?
                ''')
                input("press [ENTER] to continue")
                print('''
You concentrate as hard as you can on the mental image of Mama Bear melting. You've seen the movies, you know that to fire
lasers from your eyes you just have to will it to happen.
                ''')
                input("press [ENTER] to continue")
                Navigator = "FLE"
                break
            if gameChoice.lower() in ListMenu:
                Menu(True)
                break
            else:
                print("Please select an actual option.")

    elif str(Navigator) == "1AAABAAA":
        print('''
        
Cub Bear flies out of the house at lightning fast speeds, aiming to bite into your neck. You spin around and, like 
swatting a fly, slap Cub Bear back into the house, his impact causing an explosion that rocks the valley. A furious 
growl from the left startles you, and you bearly manage to dodge Mama Bear's murderous swipe.

"BEARNABY!" Mama Bear cries, then turns to you, "YOU HURT MY BABY!!"
        ''')
        input("press [ENTER] to continue")
        print('''
Mama Bear recklessly swings at you, fighting with every cell in her body. Her attacks are sloppy and easy to dodge, 
making this an easy fight.
She lunges at you. You dodge to the right, and with a quick strike to the back of the neck, Mama Bear goes down, 
unconscious.
        ''')
        input("press [ENTER] to continue")
        print('''
You're about to walk away, when a bright light appears in the sky. A bright, growing, bear-shaped light. Your eyes
widen, and you brace for impact right as a flaming meteor of a bear crashes into the ground at your feet, sending you 
flying.

Skidding to a halt a few meters away, you leap to your feet and quickly assess the new crater in front of you. Smoke 
fills the valley, obscuring most of the destruction from your view.
        ''')
        input("press [ENTER] to continue")
        print('''
With a blinding flash and a burst of wind, the smoke clears. A glowing, godly Bear the size of a small car floats up
from the crater before you. You recognize this bear as the one you punched into space. The bear that Mama Bear referred 
to as: 'Robearto'

        ''')
        input("press [ENTER] to continue")
        print('''
        Robearto crosses his arms, staring at you with an unreadable expression.
        
        "SO," Robearto states in a booming voice that echoes throughout the valley, you get the impression that his 
        voice alone could shatter mountains.
        
        "I take it YOU'RE the one who defeated MY Bear-atrice?"
        
        "And what if I did?" you respond, failing to hide the shaking in your voice as you face this behemoth.
        
        Robearto looms closer, floating down to eye level, inches from your face.
        ''')
        input("press [ENTER] to continue")
        print('''
        Robearto backs up from you, sighs, and bows down. 
        
        "You have bested both I and Bearatrice, the King and Queen of the Bears, in hand to hand combat. By ancient 
        bear law, you have rightfully earned the crown. I bow to you, O mighty king of bears."
        
        As Robearto utters these words, the remains of the forest around you shift and russle. Bears of every shape and
        species emerge from the bushes, surrounding you. They gather in close, hundreds upon hundreds of bears, and bow
        to you.
        
        ''')
        input("press [ENTER] to continue")
        print('''
        Over the next few months, under your leadership the Bear society really flourishes. Roads and infrastructure are
        laid down all throughout the valley, forming a sprawling network of transport that effectively triples the Bear 
        economy. With your guidance, a hospital is constructed, providing free health care to all of your citizens.
        The wrecked Bear house is converted into a school for young cubs, teaching them all the knowledge they'll need 
        to become functioning membears of society. 
        
        ''')
        input("press [ENTER] to continue")
        print('''
        Over the next few years, houses and suburbs are constructed, as well as an impressive automotive industry. 
        Cars designed for humans AND bears are produced to meet the growing demand for human-friendly vehicles and 
        buildings, as more and more of the small, struggling settlements across the nation flock to your growing city. 
        
        ''')
        input("press [ENTER] to continue")
        print('''
        To combat the increased intensity of bandit raids, especially from your old gang, the Vinter Kin, A combined 
        Bear-Human military is founded, and inventive battle tactics are devised. Within a year of this new military's 
        founding, a war breaks out between your city and the gangs. Many lives are lost, many Bears are flung, but after
        a week of fighting your military manages to storm the gang leaders and you secure a decisive victory. 
        
        ''')
        input("press [ENTER] to continue")
        print('''
        With the war won, You continue to expand your rule, branching off into new cities and towns. Finally, after 
        ten whole years, your small kingdom has blossomed into a prosperous nation of Bears and Humans that controls 
        all of north america. By now, the AshFall has dissipated and the sky is clear. 
        
        ''')
        input("press [ENTER] to continue")
        print('''
        You look out of your palace, which was once the White House, and watch as the first ambassador 
        from europe arrives at your doorstep to discuss trades.
        
        Congratulations, you have finished Fimbulvetr as King of the Bears.''')
        gameOn = 1


    elif str(Navigator) == "FB":
        deadNum = random.randint(0, 2)
        print(deadBear[deadNum])
        gameOn = 1

    elif str(Navigator) == "FD":
        deadNum = random.randint(0, 2)
        print(deadDog[deadNum])
        gameOn = 1

    elif str(Navigator) == "FLE":
        print('''
        You focus your intense bear-flinging force on the pupils off your eyes, gathering as much power as you possibly
        can. The air in front of you crackles and hisses, heating up to insane temperatures. 
        
        But, why do your eyes hurt? Why does your brain hurt?
        
        Then it hits you: Eyes ABSORB light, they don't eject light.
        
        The power builds up, you can FEEL your eyes begin to boil, but you can't stop the flow of energy. Red lightning 
        arcs from the air into your eyes, crackling aggressively. The heat becomes too much to bear, and you let go...
        ''')
        input("press [ENTER] to continue")
        print('''
        
        Like a cliche slow motion movie sequence, complete with soft opera music, your head combusts into a brilliant 
        multicoloured inferno. Searing light of all colours spreads from the beacon that is your head, scorching everything in
        a 5 mile radius. The mountain beneath your feet is flash-melted, forming a bubbling expanse of magma.
        Technicolour waves of plasma pulse outwards, melting Mama bear and the rest of the valley around you. The force 
        of the blast parts the clouds and, for a brief moment, the heat of your explosion can be felt from space.
        ''')
        input("press [ENTER] to continue")
        print('''
        Well, technically you DID cause Mama Bear to melt.
        
        You have Died.
        ''')
        gameOn = 1

    elif str(Navigator) == "FCB":
        print(''' 
        You slump to your knees, clutching your oozing stomach. Mama Bear lifts your chin so that you 
        stare directly into her eyes.
        
        "You're a tough kid, I'll give ya that," Mama Bear remarks in a grizzly tone, "But you're an 
        arrogant fool if you think you can win just because you're the protagonist."
        ''')
        input("press [ENTER] to continue")
        print('''
        Mama Bear drops your chin and begins to pace around you at a leisurely pace.
        
        "This game of life may be full of nonsense, but there is some truth and knowledge hidden behind the absurd.
        To win a fight, you must choose the correct options at the correct times, the same is true in any fight. To
        get what you want, you must EARN it, even if you fail along the way. One cannot simply walk into success, you
        must acknowledge the obstacles and opponents that block your path.
        ''')
        input("press [ENTER] to continue")
        print('''
        "You, Kid, have failed. You failed to recognize your own limits, you failed to recognize my skill, and you 
        failed to properly recognize the danger that you were in."
        
        "Next time, take a while to think through your situation, and consider ALL the options available to you.
        Got it?"
        ''')
        input("press [ENTER] to continue")
        print('''
        With that, the world around you spirals out into a misty, abyssal void. The last wisps of breath leave your
        lungs, and you let go of your mortal body.
        
        You have died.''')
        gameOn = 1

    elif str(Navigator) == "FF":
        deadNum = random.randint(0, 3)
        print(deadFlame[deadNum])
        gameOn = 1

    elif str(Navigator) == "FP":
        print('''
You become so amazed at your achievement that you forget you are beside a plane, and fly directly into its propellers.

You have died.
        ''')
        gameOn = 1

    elif str(Navigator) == "FDW":
        deadNum = random.randint(0,2)
        print(deadDrown[deadNum])
        gameOn = 1

    elif str(Navigator) == "FFS":
        print('''
I'm actually so grossed out by that. I need it to stop.

You see a giant fist form above you, just floating in midair.
        ''')
        input("press [ENTER] to continue")
        print('''
The fist slams down on your measly body and turns you into a puddle of mush. There goes the sandwich issue, and you in
the proccess.

You have died.
        ''')
    elif str(Navigator) == "FHE":
        print('''
You put your disgrace of a sandwich down on the sand, and strap that C-4 stuff you found earlier to it. This will look
awesome.
        ''')
        input("press [ENTER] to continue")
        print('''
You drive away from the beach with a smile on your face, blasting music, with a huge explosion behind you to eradicate
your sandwich as you disappear into the sunset.

Congratulations! You have completed Fimbulvetr with the 'Hollywood Explosion' ending!
        ''')
        gameOn = 1

    elif str(Navigator) == "FMB":
        print('''
        The bear crashes head first into you, crushing your lungs and chest instantaneously. The bear's flames swarm 
        around you, as you feel your body spread across the ground like jam.
        
        You have died.
        ''')
        gameOn = 1
while True:
    time.sleep(0.1)
