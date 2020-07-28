print("Hvat segirthu?")
print("Cause I'm doin fine")
print("Although I will say the Fimbulvetr is quite annoying, what with all the ashfall")

# Function Definitions

ListA = list(["A","a",'"a"','"A"'," A"," a","A ","a ",])
ListB = list(["B","b",'"b"','"B"'," B"," b","B ","b ",])
ListC = list(["C","c",'"c"','"C"'," C"," c","C ","c ",])
ListD = list(["D","d",'"d"','"D"'," D"," d","D ","d ",])


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
        print(''' Please select ONE of the following options:
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
            menuChoice = str(input("===>>"))
            if menuChoice in ListA:
                optionsCheck = open("Save File","r")
                optionsNum = int(optionsCheck.read())
                loadOptions = str(optionsCheck.read())
                print(optionsNum)
                print(loadOptions)
            elif menuChoice in ListB:
                print("bye")
            elif menuChoice in ListC:
                print("die")
            else:
                print("Type an actual option please.")


#MainGame Loop
