import time
import location_data
def invalid():
    print("Invalid choice, please try again\n")
def startup():
    quit = False
    while True:
        while True:
            name = input("What is your name? ")
            try:
                with open(name +'.txt.','r'):
                    print("Uhhh... I don't think that's your name.")
                while True:
                    print("** Would you like to continue under your previous character under that name? (Y/N)")
                    yn = input()
                    if yn == 'y':
                        return [],True
                    elif yn == 'n':
                        print("Maybe you ought to rethink your name.")
                        break
                    else:
                        print("** invalid choice, try again.")
            except FileNotFoundError:
                print("**")
                break
        print(name + "?")
        time.sleep(1)
        print("What a wonderful name!")
        time.sleep(1)
        while True:
            print("\nDo you have a specialty?")
            response = input("1. Yes\n2. What is a specialty? ")
            time.sleep(1)
            if response == '1':
                print("\nGreat! What specialty are you?\n1. Warrior\n2. Archer\n3. Mage\n4. Rogue")
                specialty = input()
                if specialty not in '1234':
                    print("Never heard of that one, I don't think that's right.")
                else:
                    break
            elif response == '2':
                print("\nA specialty is a class, you can be a Warrior, Archer, Mage, or Rogue!")
            else: 
                print("Sorry, I didn't understand what you said.")
        if specialty == '1':
            specialty = 'Warrior'
            trainer = "Brutus"
            trainer_loc = 'Arena'
        elif specialty == '2':
            specialty = 'Archer'
            trainer = "Gladiel"
            trainer_loc = 'Range'
        elif specialty == '3':
            specialty = 'Mage'
            trainer = "Marvin"
            trainer_loc = "Wizard's Tower"
        else:
            specialty = 'Rogue'
            trainer = "Thulien"
            trainer_loc = 'Tavern'
        time.sleep(1)
        print("Wow! There aren't many",specialty + "'s","around here.")
        time.sleep(1)
        print("Luckily, I know someone who can train you!")
        time.sleep(1)
        print("Their name is",trainer)
        time.sleep(1)
        while True:
            time.sleep(1)
            tf = input("Have you any more questions for me? (Y/N) ")
            if tf == "y":
                while True:
                    print("\nWhat have you got?")
                    print("\n1. What is this place anyway?\n2. Where do I find my trainer?\n3. What is your name?\n4. Nevermind")
                    choice = input()
                    if choice not in '1234':
                        print("There you go spouting nonsense again...")
                    elif choice == '1':
                        print("This land is called Mythrindor, we are currently in Mythrindor City!")
                        time.sleep(1)
                        print("The largest city in the land of the living!\n")
                        while True:
                            choice2 = input("1. Land of the living? Is there more than just the land of the living?\n2. Cool!")
                            if choice2 not in '12':
                                print("Quit it with the Jibberish!")
                            elif choice2 == '1':
                                print("Mythrindor is in the land of the living.")
                                time.sleep(1.5)
                                print("Sythlindor is in the land of the dead, and Sythlindor City is the largest city of the underworld.")
                                time.sleep(1)
                                print("They say there lies a dormant portal to the land of the dead, but we stay away from it.")
                            else: 
                                break
                    elif choice == '2':
                        print("You can find",trainer,"in the",trainer_loc)
                    elif choice == '3':
                        print("My name's Jeff.")
                    else:
                        print("Okay!")
                        break
            elif tf == "n":
                break
            else:
                print("Are you sure you know english?")
        time.sleep(1)
        print("Well, I suppose you'e off then! Good luck,", name +'!')
        print("** Whenever you see this symbol, it is the game confirming a sequence was successful. You can ignore this.")
        dictionary = {"Name" : name, "Trainer" : trainer, "Trainer Location" : trainer_loc, "Specialty" : specialty}
        return dictionary, quit

def loc(location):
    def wdywtg():
        print("Where do you want to go?")
    def invalid():
        print("Invalid choice, please try again\n")
    starts = ["Tavern","Arena","Wizard's Tower","Range","Market Square","Mythrindor Gates"]
    last_loc = location
    if location.lower() in starts.lower() and location.lower() != "mythrindor gates":
        while True:
            i = 1
            for n in starts:
                print("Where do you want to go?")
                print(i + ".",n)
                i += 1
            choice = input("Choose: ")
            if choice == '1':
                location = "Tavern"
            elif choice == '2':
                location = "Arena"
            elif choice == '3':
                location = "Wizard's Tower"
            elif choice == '4':
                location = "Range"
            elif choice == '5':
                location = "Market Square"
            elif choice == '6':
                location = "Mythrindor Gates"
            else:
                print("Invalid Choice, please try again\n")
            if choice in '123456':
                break
    if location.lower() == "mythrindor gates":
        while True:
            i = 1
            for n in starts:
                print("Where do you want to go?")
                print(i+'.',n)
                i+=1
            print(i +'.',"Old Watchtower")
            if choice == '1':
                location = "Tavern"
            elif choice == '2':
                location = "Arena"
            elif choice == '3':
                location = "Wizard's Tower"
            elif choice == '4':
                location = "Range"
            elif choice == '5':
                location = "Market Square"
            elif choice == '6':
                location = "Mythrindor Gates"
            elif choice == '7':
                location = 'Old Watchtower'
            else:
                print("Invalid Choice, please try again\n")
            if choice in '1234567':
                break
    if location.lower() == "old watchtower":
        while True:
            wdywtg()
            print("1. Mythrindor Gates")
            print("2. Western Outskirts")
            choice = input("Choose: ")
            if choice == '1':
                location = "Mythrindor Gates"
                break
            elif choice == '2':
                location = "Western Outskirts"
                break
            else:
                invalid()
    if location.lower() == "western outskirts":
        while True:
            wdywtg()
            print("1. Old Watchtower")
            print("2. Abandoned Farm")
            choice = input("Choose: ")
            if choice == '1':
                location = "Old Watchtower"
                break
            elif choice == '2':
                location = "Abandoned Farm"
                break
            else:
                invalid()
    if location.lower == 'abandoned farm':
        while True:
            wdywtg()
            print("1. Western Outskirts")
            print("2. Whispering Woods")
            print("3. Crystal Glade")
            choice = input("Choose: ")
            if choice == '1':
                location = 'Western Outskirts'
                break
            elif choice == '2':
                location = 'Whispering Woods'
                break
            elif choice == '3':
                location = "Crystal Glade"
                break
            else:
                invalid()
    if location.lower == 'whispering woods':
        while True:
            wdywtg()
            print("1. Woodsman's Hut")
            print("2. Abandoned Farm")
            choice = input("Choose: ")
            if choice == '1':
                location = "Woodsman's Hut"
                break
            elif choice == '2':
                location = "Abandoned Farm"
                break
            else:
                invalid()
    if location.lower == 'crystal glade':
        while True:
            wdywtg()
            print("1. Stonebridge Crossing")
            print("2. Abandoned Farm")
            choice = input("Choose: ")
            if choice == '1':
                location = 'Stonebridge Crossing'
                break
            elif choice == '2':
                location = 'Abandoned Farm'
            else:
                invalid()
    if location.lower == "woodsman's hut":
        while True:
            wdywtg()
            print("1. Whispering Woods")
            print("2. Stonebridge Crossing")
            choice = input("Choose: ")
            if choice == '1':
                location = 'Whispering Woods'
                break
            elif choice == '2':
                location = 'Stonebridge Crossing'
                break
            else:
                invalid()
    if location.lower == 'stonebridge crossing':
        while True:
            wdywtg()
            print("1. Woodsman's Hut")
            print("2. Crystal Glade")
            print("3. Fogmoor Marsh")
            choice = input("Choose: ")
            if choice == '1':
                location = "Woodsman's Hut"
                break
            elif choice == '2':
                location = 'Crystal Glade'
                break
            elif choice == '3':
                location = 'Fogmoor March'
                break
            else:
                invalid()
    if location.lower == 'fogmoor marsh':
        while True:
            wdywtg()
            print("1. Stonebridge Crossing")
            print("2. Marsh Depths")
            print("3. Pilgrim's Descent")
            choice = input("Choose: ")
            if choice == '1':
                location = 'Stonebridge Crossing'
                break
            elif choice == '2':
                location = 'Marsh Depths'
                break
            elif choice == '3':
                location = "Pilgrim's Descent"
                break
            else:
                invalid()
    if location.lower == 'marsh depths':
        while True:
            wdywtg()
            print("1. Fogmoor Marsh")
            choice = input("Choose: ")
            if choice == '1':
                location = "Fogmoor Marsh"
                break
            else:
                invalid()
    if location.lower == "pilgrim's descent":
        while True:
            wdywtg()
            print("1. Fogmoor Marsh")
            print("2. Cliffside Shrine")
            choice = input("Choose: ")
            if choice == '1':
                location = "Fogmoor Marsh"
                break
            elif choice == '2':
                location = 'Cliffside Shrine'
                break
            else:
                invalid()
    if location.lower == 'cliffside shrine':
        while True:
            wdywtg()
            print("1. Pilgrim's Descent")
            print("2. Blackmond Ridge")
            choice = input("Choose: ")
            if choice == '1':
                location = "Pilgrim's Descent"
                break
            elif choice == '2':
                location = 'Blackmond Ridge'
                break
            else:
                invalid()
    if location.lower == 'blackmond ridge':
        while True:
            wdywtg()
            print("1. Cliffside Shrine")
            print("2. Gates of Sythlindor")
            choice = input("Choose:")
            if choice == '1':
                location = "Cliffside Shrine"
                break
            elif choice == '2':
                location = "Gates of Sythlindor"
                break
            else:
                invalid()
    if location.lower == 'gates of sythlindor':
        while True:
            wdywtg()
            print("1. Cliffside Shrine")
            print("2. The Underworld")
            choice = input("Choose: ")
            if choice == '1':
                location = 'Cliffside Shrine'
                break
            elif choice == '2':
                location = "Underworld"
            else:
                invalid()
    if location.lower == 'underworld':
        while True:
            wdywtg()
            print("1. Gates of Sythlindor")
            print("2. Portal to Mythrindor City")
            choice = input("Choose: ")
            if choice == '1':
                location = 'Gates of Sythlindor'
                break
            elif choice == '2':
                location = 'Mythrindor Gates'
                break
            else:
                invalid()
    return location, last_loc


def inv():
    return

def combat():
    return

def enemies():
    return