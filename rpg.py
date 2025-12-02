# My text-style RPG Game
# by Jayven
# 11/24/25

# THINGS TO WORK ON:

# PRIORITY LIST:
# !!! Change character info to a dictionary. [COMPLETED 12/1/25]
# !! response.lower() for all inputs. [COMPLETED 12/1/25]
# 1. combat function
# 2. inventory access
# 3. currency tracking
# 4. trading
# 5. dungeons in select locations
# 6. crafting?

# Character info order:
# name, trainer, trainer_loc, specialty

# Character state order:
# location, last location, health, max health, level, xp.

# 

#Boot up:

import rpg_functions as r
import json
flag = 1
char_info = {}
char_state = {}
char_inventory = {}
char_equipped = {}
character = {'info' : char_info, 'state' : char_state, 'inv' : char_inventory, 'equipped' : char_equipped}
quit = False
while True:
    print("Welcome to the Jayven's RPG Game!")
    print("\nWould you like to:")
    print("1. Start a new game")
    print("2. Continue a saved game")
    print("3. Quit")
    print("Note: If you want to delete a character, you must delete the character's txt files.")
    choice = input("Choose: ")
    if choice == '1':
        while True:
            info, quit = r.startup()
            char_info.update(info)
            char_state.update({'location' : 'Market Square', 'last location' : 'Market Square', 'hp' : 10, 'max hp' : 10, 'lvl' : 1, 'xp' : 0})
            if quit == True:
                break
            with open(char_info['Name'] + '.txt', 'w') as i:
                json.dump(character, i)
            break    
        break
    elif choice == '2':
        file = input("What is the name of the character you would like to continue? ")
        try:
            with open(file.lower() + '.txt','r'):
                print("Character found!")
                file = file.lower + '.txt'
                with open(file, 'r') as f:
                    character = json.load(f)
                char_info = character['info']
                char_state = character['state']
                char_inventory = character['inv']
                char_equipped = character['equipped']
            break
        except FileNotFoundError:
            print("File not found, please try again")
    elif choice == '3':
        print("Quitting.")
        quit = True
        break
    else:
        print("Invalid choice, please try again")
if quit == True:
    print("Goodbye!")
else:
    while quit == False:
        print("Current Location:",char_state['location'])
        while True:
            if flag == 1: #1 = after movement
                print("What would you like to do?"
                    "\n1. Move Locations"
                    "\n2. Check Inventory"
                    "\n3. Check Character Info"
                    "\n4. Go into " + character['state']['location'] + "."
                "\n5. Quit Game")
                choice = input("Choose: ")
                if choice == '1':
                    location, last_loc = r.loc(character['state']['location'])
                    character['state']['location'] = location
                    character['state']['last location'] = last_loc
                    break
                elif choice == '2':
                    r.inv()
                    break
                elif choice == '3':
                    for info in character['info']:
                        print(info + ":", character['info'][info])
                    break
                elif choice == '4':
                    # Placeholder for going into the current location
                    print("You go into", character['state']['location'])
                    break
                elif choice == '5':
                    print("Quitting game...")
                    quit = True
                    break
                else:
                    r.invalid()
                break