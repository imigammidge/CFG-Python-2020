# CFG Project - JP, Imi & Kristina 

# FLASK CODE
# FYI - Imi - Imported Flask for web-based app

from app import start_flask
import sys


use_flask = input("Would you like to use the web-based version? [Y/N] ").strip().upper()
if use_flask == "Y":
    start_flask()

# FLASK CODE [END]

print() # Pokémon Ascii art game header
print(
        "                                ,'\                                  "
    )
print(
        " _.----.        ____         ,'  _\   ___    ___     ____            "
    )
print(
        "_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.   "
    )
print(
        "\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |  "
    )
print(
        "\.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |   "
    )
print(
        " \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |    "
    )
print(
        "  \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |    "
    )
print(
        "   \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |    "
    )
print(
        "    \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |    "
    )
print(
        "     \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |    "
    )
print(
        "      \_.-'       |__|    `-._ |              '-.|     '-.| |   |    "
    )
print(
        "                              `'                            '-._|    "
    )
print()

# Needed to make the function work when called via dictionary
#def print_pokemon(pokemon):
#    pokemon_art[pokemon]()

import random
import time
import sys

# Delay printing to look like a GameBoy - just put delay_print in front of text
def delay_print(s):
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

# Welcome
print("~~ Welcome to the world of Pokémon! ~~ \n")
player1name = input("Please enter your name: ")
print()
delay_print("Hello " + player1name + ", get ready to enter the world of Pokémon!\n")

# Storyline Intro
print()
delay_print('You are a Pokémon trainer destined to fight 5 battles.')
time.sleep(1)
delay_print(' These battles will take place at various locations in  Kanto.')
time.sleep(1)
delay_print(' The last 3 will be against Gym Leaders.')
time.sleep(1)
delay_print(' Only if the final Gym Leader is defeated do you win the game and become a Pokémon Master.')
time.sleep(1)

# Do you accept the game? 'Yes' takes user to Pallet Town and then their first battle, 'no' ends the game

accept = input(' Do you accept? (y/n) ').lower()  # FYI .lower means that even if user types captial Y it reads it as lower case
if accept.lower() == 'y':
    delay_print(''+ player1name + ', you have accepted the challenge! Let\'s go to Pallet Town.')
    print() # Pallet town ascii art
    print()
    print('                                                           |>>>                 ')
    print('                   _                      _                |                    ') 
    print('    ____________ .' '.    _____/----/-\ .' './========\   / \                   ')
    print('   //// ////// /V_.-._\  |.-.-.|===| _ |-----| u    u |  /___\                  ')
    print('  // /// // ///==\ u |.  || | ||===||||| |T| |   ||   | .| u |_ _ _ _ _ _       ')
    print(' ///////-\////====\==|:::::::::::::::::::::::::::::::::::|u u| U U U U U        ')
    print(' |u u|u | |u ||||||..|               ::::::::            |===|>=== _ _ ==       ')
    print(' |===|  |u|==|++++|==|              .::::::::.           | T |....| V |..       ')
    print(' |u u|u | |u ||HH||         \|/    .::::::::::.                                 ')
    print(' |===|_.|u|_.|+HH+|_              .::::::::::::.              _                 ')
    print('                __(_)___         .::::::::::::::.         ___(_)__              ')
    print('---------------/  / \  /|       .:::::;;;:::;;:::.       |\  / \  \-------      ')
    print('______________/_______/ |      .::::::;;:::::;;:::.      | \_______\________    ')
    print('|       |     [===  =] /|     .:::::;;;::::::;;;:::.     |\ [==  = ]   |        ')
    print('|_______|_____[ = == ]/ |    .:::::;;;:::::::;;;::::.    | \[ ===  ]___|____    ')
    print('     |       |[  === ] /|   .:::::;;;::::::::;;;:::::.   |\ [=  ===] |          ')
    print('_____|_______|[== = =]/ |  .:::::;;;::::::::::;;;:::::.  | \[ ==  =]_|______    ')
    print(' |       |    [ == = ] /| .::::::;;:::::::::::;;;::::::. |\ [== == ]      |     ')
    print('_|_______|____[=  == ]/ |.::::::;;:::::::::::::;;;::::::.| \[  === ]______|_    ')
    print('   |       |  [ === =] /.::::::;;::::::::::::::;;;:::::::.\ [===  =]   |        ')
    print('___|_______|__[ == ==]/.::::::;;;:::::::::::::::;;;:::::::.\[=  == ]___|_____   ')
    print()
else:
    delay_print(''+ player1name + ', you have not accepted the challenge.')
    print() # Game over
    print()
    print('_______  _______  __   __  _______    _______  __   __  _______  ______    ')  
    print('|       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  ')
    print('|    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  ')
    print('|   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ ')
    print('|   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |')
    print('|   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |')
    print('|_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|')
    print()
    exit ()
time.sleep(1)

print() # This makes a new line / space between lines
delay_print("Welcome to Pallet Town. This is your hometown and the beginning of your journey. You have been given 6 Pokémon.")
time.sleep(1)
delay_print(" It's time to set off on your adventure!")
print()
time.sleep(1)
delay_print("")
time.sleep(1)

# Battle 1 - Pallet Town
print() 
print('  ────────────────────────────────    ⋞ 〈 ⏣ 〉 ⋟    ────────────────────────────────  ')
print()
delay_print("Battle 1 - Pallet Town.")
print()
time.sleep(1)

# Pallet Town Battle Intro
print()
delay_print(''+ player1name + ', both you and your hometown Rival, Blue Oak, want to take Route 1 North onto Viridian City. However, only one of you can continue on this journey. Your first Battle begins now...')
print()
print()
time.sleep(1)

# JP
import random
import requests
def generate_player_party():

    player_party = []

    for player_mon in range(0, 6):
        player_random_pokemon = random.randint(1, 151)
        player_party.append(player_random_pokemon)

    #delay_print(player_party)

# Player Party Pokemon - Request from PokeAPI - list of party pokemon (names)

    player_pokemon = []

# Pokemon 1

    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(player_party[0])

    response = requests.get(url)
    pokemon = response.json()

    player_pokemon.append(pokemon['name'])

# Pokemon 2

    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(player_party[1])

    response = requests.get(url)
    pokemon = response.json()

    player_pokemon.append(pokemon['name'])

# Pokemon 3

    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(player_party[2])

    response = requests.get(url)
    pokemon = response.json()

    player_pokemon.append(pokemon['name'])

# Pokemon 4

    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(player_party[3])

    response = requests.get(url)
    pokemon = response.json()

    player_pokemon.append(pokemon['name'])

# Pokemon 5

    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(player_party[4])

    response = requests.get(url)
    pokemon = response.json()

    player_pokemon.append(pokemon['name'])

# Pokemon 6

    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(player_party[5])

    response = requests.get(url)
    pokemon = response.json()

    player_pokemon.append(pokemon['name'])
    return player_pokemon

# Battle 1 - Pallet Town VS hometown Rival Blue Oak
player_party = generate_player_party()
delay_print('Your 6 Pokémon are: {}'.format(player_party))
print()

def battle_1():
# Rival 1 pokemon selection: the very first form of pokemon, i.e. the weaker versions
    opponent_team = [1, 4, 7, 10, 14, 16, 19, 21, 23, 29, 32, 37, 39, 41, 46, 48, 58, 60, 98, 116, 118, 133, 138, 147]
    opponent_choice = random.choice(opponent_team)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(opponent_choice)

    response = requests.get(url)
    pokemon = response.json()

    opponent_poke_name = pokemon["name"]
    opponent_poke_xp = pokemon["base_experience"]
    opponent_poke_weight = pokemon["weight"]
    opponent_poke_height = pokemon["height"]

    print()
    delay_print("Your Rival, Blue Oak, has chosen to attack with {}. ".format(opponent_poke_name))
    #delay_print_pokemon("{}".format(opponent_choice))
    print()

    # Rival attributes
    print()
    player_choice = input("Which Pokémon do you want to attack with? " + "\n""{}".format(player_party))

    print()
    delay_print("You have chosen to attack with {}.".format(player_choice))
    #delay_print_pokemon("{}".format(player_choice))
    print()

    delay_print("Your chosen Pokémon {} has the following attributes:".format(player_choice))

    print()
    print("╭──────────────────────────────╮")
    print("                               |")
    print("            {}                ".format(player_choice.capitalize()))
    print("|                              |")
    print("╰──────────────────────────────╯")

    # Get the xp, height, weight and maybe some more stuff?

    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(player_choice)

    response = requests.get(url)
    pokemon = response.json()

    player_poke_xp = pokemon["base_experience"]
    player_poke_weight = pokemon["weight"]
    player_poke_height = pokemon["height"]

    print("╭──────────────────────────────╮")
    print("|                              |")
    delay_print(" ---> [1] XP: {}".format(player_poke_xp)+"\n")
    delay_print(" ---> [2] Height: {}".format(player_poke_height)+"\n")
    delay_print(" ---> [3] Weight: {}".format(player_poke_weight)+"\n")
    print("|                              |")
    print("╰──────────────────────────────╯")

    print()
    player_attack = input("Which attribute do you want to use in battle (1/2/3)? ")

    if player_attack == "1":
        if player_poke_xp > opponent_poke_xp:
            delay_print("Your Pokémon XP is {}. Your Rival, Blue Oak's Pokémon XP is {}. You WIN! \n The attributes of all Pokémon in your party have increased by 10 points. Let's continue on to your second battle!".format(player_poke_xp, opponent_poke_xp))
        else:
            delay_print("Your Pokémon XP is {}. Your Rival, Blue Oak's Pokémon XP is {}. You LOSE! ".format(player_poke_xp, opponent_poke_xp))
            print()
            want_to_continue = input('Do you want to try this battle again? (y/n) ' .lower()) 

            if want_to_continue.lower() == 'y':
              delay_print("{}, let’s try this battle again!".format(player1name))
              print()
              battle_1()
            else:
              delay_print("{}, you have not won this battle.".format(player1name))
              print() # Game over
              print()
              print('_______  _______  __   __  _______    _______  __   __     _______  ______    ')  
              print('|       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  ')
              print('|    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  ')
              print('|   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ ')
              print('|   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |')
              print('|   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |')
              print('|_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|')
              print()
              exit ()
            time.sleep(1)
            
    if player_attack == "2":
        if player_poke_height > opponent_poke_height:
            delay_print("Your Pokémon height is {}. Your Rival, Blue Oak's Pokémon height is {}. You WIN! The attributes of all Pokémon in your party have increased by 10 points. Let's continue on to your second battle!".format(player_poke_height, opponent_poke_height))
        else:
            delay_print("Your Pokémon height is {}. Your Rival, Blue Oak's Pokémon height is {}. You LOSE!".format(player_poke_height, opponent_poke_height))
            print()
            want_to_continue = input('Do you want to try this battle again? (y/n) ' .lower()) 

            if want_to_continue.lower() == 'y':
              delay_print("{}, let’s try this battle again!".format(player1name))
              print()
              battle_1()
            else:
              delay_print("{}, you have not won this battle.".format(player1name))
              print() # Game over
              print()
              print('_______  _______  __   __  _______    _______  __   __     _______  ______    ')  
              print('|       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  ')
              print('|    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  ')
              print('|   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ ')
              print('|   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |')
              print('|   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |')
              print('|_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|')
              print()
              exit ()
            time.sleep(1)
            
    if player_attack == "3":
        if player_poke_weight > opponent_poke_weight:
            delay_print("Your Pokémon weight is {}. Your Rival, Blue Oak's Pokémon weight is {}. You WIN! The attributes of all Pokémon in your party have increased by 10 points. Let's continue on to your second battle!".format(player_poke_weight, opponent_poke_weight))
        else:
            delay_print("Your Pokémon weight is {}. Your Rival, Blue Oak's Pokémon weight is {}. You LOSE!".format(player_poke_weight, opponent_poke_weight))
            print()
            want_to_continue = input('Do you want to try this battle again? (y/n) '.lower()) 

            if want_to_continue.lower() == 'y':
              delay_print("{}, let’s try this battle again!".format(player1name))
              print()
              battle_1()
            else:
              delay_print("{}, you have not won this battle.".format(player1name))
              print() # Game over
              print()
              print('_______  _______  __   __  _______    _______  __   __     _______  ______    ')  
              print('|       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  ')
              print('|    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  ')
              print('|   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ ')
              print('|   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |')
              print('|   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |')
              print('|_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|')
              print()
              exit ()
            time.sleep(1)
            
battle_1()

# Battle 2 - Viridian City VS Rival Jessie
print() 
print() 
print('  ────────────────────────────────    ⋞ 〈 ⏣ 〉 ⋟    ────────────────────────────────  ')
print()
delay_print("Battle 2 - Viridian City.")
print()
time.sleep(1)

print() # Viridian City Gym ascii art
print()
print('                                                                            ')
print('   `,.      .   .        *   .    .      .  _    ..          .              ')
print('     \,~-.         *           .    .       ))       *    .                 ')
print('          \ *          .   .   |    *  . .  ~    .      .  .  ,             ')
print(' ,           `-.  .            :               *           ,-               ')
print('  -             `-.        *._/_\_.       .       .   ,-                    ')
print('  -                 `-_.,     |n|     .      .       ;                      ')
print('    -                    \ ._/_,_\_.  .          . ,          ,             ')
print('     -                    `-.|.n.|      .   ,-.__,          -               ')
print('      -                   ._/_,_,_\_.    ,-               -                 ')
print('      -                     |..n..|-`-                -                     ')
print('       -                 ._/_,_,_,_\_.                 -                    ')
print('         -               ,-|...n...|                  -                     ')
print('           -         ,- ._/_,_,_,_,_\_.              -                      ')
print('             -  ,-=-      |....n....|              -                        ')
print('              -;       ._/_,_,_,_,_,_\_.         -                          ')
print('             ,-          |.....n.....|          -                           ')
print('           ,;         ._/_,_,_,_,_,_,_\_.         -                         ')
print('  `,   .  `.  ".  `,   .| n   ,-.   n |  ",  `.  `,   .  `                  ')
print(',.:;..;;..;;.,:;,.;:,o__|__o !.|.! o__|__o;,.:;.,;;,,:;,.:;,;;:             ')
print(' ][  ][  ][  ][  ][  |_i_i_H_|_|_|_H_i_i_|  ][  ][  ][  ][  ][              ')
print('                     |     //=====\\     |                                  ')
print('                     |____//=======\\____|                                  ')
print('                         //=========\\                                      ')
print()

# Viridian City Battle Intro
print()
delay_print(''+ player1name + ', welcome to Viridian City. It\'s time to pay a visit to the Gym, however, you find that the door to the Gym is locked. Your new Rival, Jessie, is blocking the door and the key is in their hand. Time to prepare for your second battle...')
print()
print()
time.sleep(1)

# Battle 2
def battle_2():
    # Rival
    opponent_team = [2, 5, 8, 11, 14, 17, 20, 30, 33, 44, 61, 64, 67, 70, 91, 93, 148]
    opponent_choice = random.choice(opponent_team)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(opponent_choice)

    response = requests.get(url)
    pokemon = response.json()

    opponent_poke = pokemon["name"]
    opponent_poke_xp = pokemon["base_experience"]
    opponent_poke_weight = pokemon["weight"]
    opponent_poke_height = pokemon["height"]

    delay_print("Your Rival, Jessie, has chosen to attack with {}. ".format(opponent_poke))
    #delay_print_pokemon("{}".format(opponent_choice))
    print()
    #Player
    print()
    player_choice = input("Which Pokémon do you want to attack with? " "\n""{}".format(player_party))

    print()
    delay_print("You have chosen to attack with {}.".format(player_choice))
    #delay_print_pokemon("{}".format(player_choice))
    print()

    delay_print("Your chosen Pokémon {} has the following attributes: ".format(player_choice))

    print()
    print("╭──────────────────────────────╮")
    print("                               |")
    print("            {}                  ".format(player_choice.capitalize()))
    print("|                              |")
    print("╰──────────────────────────────╯")

    #Level 2 attributes

    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(player_choice)

    response = requests.get(url)
    pokemon = response.json()

    player_poke_xp_2 = pokemon["base_experience"] + 10
    player_poke_weight_2 = pokemon["weight"] + 10
    player_poke_height_2 = pokemon["height"] + 10

    print("╭──────────────────────────────╮")
    print("                               |")
    delay_print(" ---> [1] XP: {}".format(player_poke_xp_2)+"\n")
    delay_print(" ---> [2] Height: {}".format(player_poke_height_2)+"\n")
    delay_print(" ---> [3] Weight: {}".format(player_poke_weight_2)+"\n")
    print("|                              |")
    print("╰──────────────────────────────╯")
    print()

    player_attack = input("Which attribute do you want to use in battle (1/2/3)? ")

    if player_attack == "1":
        if player_poke_xp_2 > opponent_poke_xp:
            delay_print("Your Pokémon XP is {}. Your Rival, Jessie's Pokémon XP is {}. You WIN! The attributes of all Pokémon in your party have increased by 10 points.".format(player_poke_xp_2, opponent_poke_xp))
            print() # Won the battle & got the Gym key
            print()
            delay_print('Congratulations, the key to the Gym is yours!')
            print()
            print()
            print('8 8 8 8                       ooo         ')
            print('8a8 8a8                    oP     ?b      ')    
            print('d888a888zzzzzzzzzzzzzzzzzzz8       8b     ')
            print('  ^                         ?o___oP       ')
            print()
        else:
            delay_print("Your Pokémon XP is {}. Your Rival, Jessie's Pokémon XP is {}. You LOSE! ".format(player_poke_xp_2, opponent_poke_xp))
            print()
            want_to_continue = input('Do you want to try this battle again? (y/n) ' .lower()) 

            if want_to_continue.lower() == 'y':
              delay_print("{}, let’s try this battle again!".format(player1name))
              print()
              battle_2()
            else:
              delay_print("{}, you have not won this battle.".format(player1name))
              print() # Game over
              print()
              print('_______  _______  __   __  _______    _______  __   __     _______  ______    ')  
              print('|       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  ')
              print('|    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  ')
              print('|   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ ')
              print('|   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |')
              print('|   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |')
              print('|_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|')
              print()
              exit ()
            time.sleep(1)
            
    if player_attack == "2":
        if player_poke_height_2 > opponent_poke_height:
            delay_print("Your Pokémon height is {}. Your Rival, Jessie's Pokémon height is {}. You WIN! The attributes of all Pokémon in your party have increased by 10 points.".format(player_poke_height_2, opponent_poke_height))
            print() # Won the battle & got the Gym key
            print()
            delay_print('Congratulations, the key to the Gym is yours!')
            print()
            print()
            print('8 8 8 8                       ooo         ')
            print('8a8 8a8                    oP     ?b      ')    
            print('d888a888zzzzzzzzzzzzzzzzzzz8       8b     ')
            print('  ^                         ?o___oP       ')
            print()
        else:
            delay_print(
                "Your Pokémon height is {}. Your Rival, Jessie's Pokémon height is {}. You LOSE!".format(player_poke_height_2, opponent_poke_height))
            print()
            want_to_continue = input('Do you want to try this battle again? (y/n) ' .lower()) 

            if want_to_continue.lower() == 'y':
              delay_print("{}, let’s try this battle again!".format(player1name))
              print()
              battle_2()
            else:
              delay_print("{}, you have not won this battle.".format(player1name))
              print() # Game over
              print()
              print('_______  _______  __   __  _______    _______  __   __     _______  ______    ')  
              print('|       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  ')
              print('|    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  ')
              print('|   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ ')
              print('|   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |')
              print('|   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |')
              print('|_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|')
              print()
              exit ()
            time.sleep(1)
            
    if player_attack == "3":
        if player_poke_weight_2 > opponent_poke_weight:
            delay_print("Your Pokémon weight is {}. Your Rival, Jessie's Pokémon weight is {}. You WIN! The attributes of all Pokémon in your party have increased by 10 points.".format(player_poke_weight_2, opponent_poke_weight))
            print() # Won the battle & got the Gym key
            print()
            delay_print('Congratulations, the key to the Gym is yours!')
            print()
            print()
            print('8 8 8 8                       ooo         ')
            print('8a8 8a8                    oP     ?b      ')    
            print('d888a888zzzzzzzzzzzzzzzzzzz8       8b     ')
            print('  ^                         ?o___oP       ')
            print()
        else:
            delay_print(
                "Your Pokémon weight is {}. Your Rival, Jessie's Pokémon weight is {}. You LOSE!".format(player_poke_weight_2, opponent_poke_weight))
            print()
            want_to_continue = input('Do you want to try this battle again? (y/n) '.lower()) 

            if want_to_continue.lower() == 'y':
              delay_print("{}, let’s try this battle again!".format(player1name))
              print()
              battle_2()
            else:
              delay_print("{}, you have not won this battle.".format(player1name))
              print() # Game over
              print()
              print('_______  _______  __   __  _______    _______  __   __     _______  ______    ')  
              print('|       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  ')
              print('|    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  ')
              print('|   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ ')
              print('|   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |')
              print('|   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |')
              print('|_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|')
              print()
              exit ()
            time.sleep(1)
battle_2()  

# Battle 3 - Viridian Forest VS Viridian City Gym Leader Giovanni
print()
print() 
print('  ────────────────────────────────    ⋞ 〈 ⏣ 〉 ⋟    ────────────────────────────────  ')
print()
delay_print("Battle 3 - Viridian Forest.")
print()
time.sleep(1)

# Viridian Forest ascii art?

# Viridian Forest Battle Intro
print()
delay_print(''+ player1name + ', well done, you defeated your Rival, Jessie, and made it into the Gym. Now to make it into Viridian Forest, you must defeat the Viridian City Gym Leader, Giovanni. Time to prepare for your third battle...')
print()
print()
time.sleep(1)

# Battle 3 - needs to be edited 

def battle_3():
    # Rival: Gym Leader
    opponent_team = [3, 6, 9, 12, 15, 18, 21, 31, 34, 45, 62, 65, 68, 71, 92, 94, 149]
    opponent_choice = random.choice(opponent_team)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(opponent_choice)

    response = requests.get(url)
    pokemon = response.json()

    opponent_poke = pokemon["name"]
    opponent_poke_xp = pokemon["base_experience"]
    opponent_poke_weight = pokemon["weight"]
    opponent_poke_height = pokemon["height"]

    delay_print("The Gym Leader, Giovanni, has chosen to attack with {}. ".format(opponent_poke))
    #delay_print_pokemon("{}".format(opponent_choice))
    print()
    print()
    #Player
    player_choice = input("Which Pokémon do you want to attack with? " "\n""{}".format(player_party))

    print()
    delay_print("You have chosen to attack with {}.".format(player_choice))
    #delay_print_pokemon("{}".format(player_choice))
    print()

    delay_print("Your chosen Pokémon {} has the following attributes: ".format(player_choice))

    print()
    print("╭──────────────────────────────╮")
    print("|                              |")
    print("            {}                  ".format(player_choice.capitalize()))
    print("|                              |")
    print("╰──────────────────────────────╯")

    #Level 2 attributes

    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(player_choice)

    response = requests.get(url)
    pokemon = response.json()

    player_poke_xp_3 = pokemon["base_experience"] + 20
    player_poke_weight_3 = pokemon["weight"] + 20
    player_poke_height_3 = pokemon["height"] + 20

    print("╭──────────────────────────────╮")
    print("|                              |")
    delay_print(" ---> [1] XP: {}".format(player_poke_xp_3)+"\n")
    delay_print(" ---> [2] Height: {}".format(player_poke_height_3)+"\n")
    delay_print(" ---> [3] Weight: {}".format(player_poke_weight_3)+"\n")
    print("|                              |")
    print("╰──────────────────────────────╯")
    print()

    player_attack = input("Which attribute do you want to use in battle (1/2/3)? ")

    if player_attack == "1":
        if player_poke_xp_3 > opponent_poke_xp:
            delay_print("Your Pokémon XP is {}. The Gym Leader, Giovanni's Pokémon XP is {}. You WIN! The attributes of all Pokémon in your party have increased by 10 points.".format(player_poke_xp_3, opponent_poke_xp))
        else:
            delay_print("Your Pokémon XP is {}. The Gym Leader, Giovanni's Pokémon XP is {}. You LOSE! ".format(player_poke_xp_3, opponent_poke_xp))
            print()
            want_to_continue = input('Do you want to try this battle again? (y/n) ' .lower()) 

            if want_to_continue.lower() == 'y':
              delay_print("{}, let’s try this battle again!".format(player1name))
              print()
              battle_3()
            else:
              delay_print("{}, you have not won this battle.".format(player1name))
              print() # Game over
              print()
              print('_______  _______  __   __  _______    _______  __   __     _______  ______    ')  
              print('|       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  ')
              print('|    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  ')
              print('|   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ ')
              print('|   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |')
              print('|   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |')
              print('|_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|')
              print()
              exit ()
            time.sleep(1)
            
    if player_attack == "2":
        if player_poke_height_3 > opponent_poke_height:
            delay_print("Your Pokémon height is {}. The Gym Leader, Giovanni's Pokémon height is {}. You WIN! The attributes of all Pokémon in your party have increased by 10 points.".format(player_poke_height_3, opponent_poke_height))
        else:
            delay_print(
                "Your Pokémon height is {}. The Gym Leader, Giovanni's Pokémon height is {}. You LOSE!".format(player_poke_height_3, opponent_poke_height))
            print()
            want_to_continue = input('Do you want to try this battle again? (y/n) ' .lower()) 

            if want_to_continue.lower() == 'y':
              delay_print("{}, let’s try this battle again!".format(player1name))
              print()
              battle_3()
            else:
              delay_print("{}, you have not won this battle.".format(player1name))
              print() # Game over
              print()
              print('_______  _______  __   __  _______    _______  __   __     _______  ______    ')  
              print('|       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  ')
              print('|    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  ')
              print('|   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ ')
              print('|   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |')
              print('|   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |')
              print('|_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|')
              print()
              exit ()
            time.sleep(1)
            
    if player_attack == "3":
        if player_poke_weight_3 > opponent_poke_weight:
            delay_print("Your Pokémon weight is {}. The Gym Leader, Giovanni's Pokémon weight is {}. You WIN! The attributes of all Pokémon in your party have increased by 10 points.".format(player_poke_weight_3, opponent_poke_weight))
        else:
            delay_print(
                "Your Pokémon weight is {}. The Gym Leader, Giovanni's Pokémon weight is {}. You LOSE!".format(player_poke_weight_3, opponent_poke_weight))
            print()
            want_to_continue = input('Do you want to try this battle again? (y/n) '.lower()) 

            if want_to_continue.lower() == 'y':
              delay_print("{}, let’s try this battle again!".format(player1name))
              print()
              battle_3()
            else:
              delay_print("{}, you have not won this battle.".format(player1name))
              print() # Game over
              print()
              print('_______  _______  __   __  _______    _______  __   __     _______  ______    ')  
              print('|       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  ')
              print('|    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  ')
              print('|   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ ')
              print('|   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |')
              print('|   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |')
              print('|_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|')
              print()
              exit ()
            time.sleep(1)
battle_3()  

# Battle 4 - Pewter City VS Gym Leader Brock
print()
print() 
print('  ────────────────────────────────    ⋞ 〈 ⏣ 〉 ⋟    ────────────────────────────────  ')
print()
delay_print("Battle 4 - Pewter City.")
print()
time.sleep(1)

# Pewter City Battle Intro
print()
delay_print(''+ player1name + ', congratulations, you have defeated the Viridian City Gym Leader, Giovanni. It\'s time to make your way through Viridian Forest onto Pewter City. Here you will meet your Rival and Gym Leader, Brock. Time to prepare for your penultimate battle...')
print()
print()
time.sleep(1)

# Battle 4 - Pewter City VS Brock (needs to be edited)

def battle_4():
    # Rival: Gym Leader
    opponent_team = [6, 10, 18, 24, 30, 36, 42, 61, 35, 47, 66, 64, 75, 76, 99, 96, 150]
    opponent_choice = random.choice(opponent_team)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(opponent_choice)

    response = requests.get(url)
    pokemon = response.json()

    opponent_poke = pokemon["name"]
    opponent_poke_xp = pokemon["base_experience"]
    opponent_poke_weight = pokemon["weight"]
    opponent_poke_height = pokemon["height"]

    delay_print("The Gym Leader, Brock, has chosen to attack with {}. ".format(opponent_poke))
    #delay_print_pokemon("{}".format(opponent_choice))
    print()
    #Player
    print()
    player_choice = input("Which Pokémon do you want to attack with? " "\n""{}".format(player_party))

    print()
    delay_print("You have chosen to attack with {}.".format(player_choice))
    #delay_print_pokemon("{}".format(player_choice))
    print()

    delay_print("Your chosen Pokémon {} has the following attributes: ".format(player_choice))

    print()
    print("╭──────────────────────────────╮")
    print("|                              |")
    print("            {}                  ".format(player_choice.capitalize()))
    print("|                              |")
    print("╰──────────────────────────────╯")

    #Level 2 attributes

    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(player_choice)

    response = requests.get(url)
    pokemon = response.json()

    player_poke_xp_3 = pokemon["base_experience"] + 30
    player_poke_weight_3 = pokemon["weight"] + 30
    player_poke_height_3 = pokemon["height"] + 30

    print("╭──────────────────────────────╮")
    print("|                              |")
    delay_print(" ---> [1] XP: {}".format(player_poke_xp_3)+"\n")
    delay_print(" ---> [2] Height: {}".format(player_poke_height_3)+"\n")
    delay_print(" ---> [3] Weight: {}".format(player_poke_weight_3)+"\n")
    print("|                              |")
    print("╰──────────────────────────────╯")
    print()

    player_attack = input("Which attribute do you want to use in battle (1/2/3)? ")

    if player_attack == "1":
        if player_poke_xp_3 > opponent_poke_xp:
            delay_print("Your Pokémon XP is {}. The Gym Leader, Brock's Pokémon XP is {}. You WIN! The attributes of all Pokémon in your party have increased by 20 points.".format(player_poke_xp_3, opponent_poke_xp))
        else:
            delay_print("Your Pokémon XP is {}. The Gym Leader, Brock's Pokémon XP is {}. You LOSE! ".format(player_poke_xp_3, opponent_poke_xp))
            print()
            want_to_continue = input('Do you want to try this battle again? (y/n) ' .lower()) 

            if want_to_continue.lower() == 'y':
              delay_print("{}, let’s try this battle again!".format(player1name))
              print()
              battle_3()
            else:
              delay_print("{}, you have not won this battle.".format(player1name))
              print() # Game over
              print()
              print('_______  _______  __   __  _______    _______  __   __     _______  ______    ')  
              print('|       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  ')
              print('|    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  ')
              print('|   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ ')
              print('|   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |')
              print('|   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |')
              print('|_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|')
              print()
              exit ()
            time.sleep(1)
            
    if player_attack == "2":
        if player_poke_height_3 > opponent_poke_height:
            delay_print("Your Pokémon height is {}. The Gym Leader, Brock's Pokémon height is {}. You WIN! The attributes of all Pokémon in your party have increased by 20 points.".format(player_poke_height_3, opponent_poke_height))
        else:
            delay_print(
                "Your Pokémon height is {}. The Gym Leader, Brock's Pokémon height is {}. You LOSE!".format(player_poke_height_3, opponent_poke_height))
            print()
            want_to_continue = input('Do you want to try this battle again? (y/n) ' .lower()) 

            if want_to_continue.lower() == 'y':
              delay_print("{}, let’s try this battle again!".format(player1name))
              print()
              battle_3()
            else:
              delay_print("{}, you have not won this battle.".format(player1name))
              print() # Game over
              print()
              print('_______  _______  __   __  _______    _______  __   __     _______  ______    ')  
              print('|       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  ')
              print('|    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  ')
              print('|   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ ')
              print('|   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |')
              print('|   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |')
              print('|_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|')
              print()
              exit ()
            time.sleep(1)
            
    if player_attack == "3":
        if player_poke_weight_3 > opponent_poke_weight:
            delay_print("Your Pokémon weight is {}. The Gym Leader, Brock's Pokémon weight is {}. You WIN! The attributes of all Pokémon in your party have increased by 20 points.".format(player_poke_weight_3, opponent_poke_weight))
        else:
            delay_print(
                "Your Pokémon weight is {}. The Gym Leader, Brock's Pokémon weight is {}. You LOSE!".format(player_poke_weight_3, opponent_poke_weight))
            print()
            want_to_continue = input('Do you want to try this battle again? (y/n) '.lower()) 

            if want_to_continue.lower() == 'y':
              delay_print("{}, let’s try this battle again!".format(player1name))
              print()
              battle_3()
            else:
              delay_print("{}, you have not won this battle.".format(player1name))
              print() # Game over
              print()
              print('_______  _______  __   __  _______    _______  __   __     _______  ______    ')  
              print('|       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  ')
              print('|    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  ')
              print('|   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ ')
              print('|   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |')
              print('|   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |')
              print('|_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|')
              print()
              exit ()
            time.sleep(1)
battle_4()  

# Battle 5 - Fighting Dojo - maybe choose between which Gym Leader to battle Giovanni / Brock or Misty?
print() 
print() 
print('  ────────────────────────────────    ⋞ 〈 ⏣ 〉 ⋟    ────────────────────────────────  ')
print()
delay_print("Battle 5 - The Fighting Dojo.")
print()
time.sleep(1)

# Fighting Dojo Battle Intro
print()
delay_print(''+ player1name + ', congratulations on defeating the Gym Leader, Brock. You are now ready to enter the Fighting Dojo. Here, you will choose which Gym Leader to face in your Final Battle. Get ready, your Final Battle starts now...')
print()
print()
time.sleep(1)

final_battle = input('Which Gym Leader do you wish to challenge in your Final Battle? [1] Giovanni, [2] Brock, [3] Misty ')
print()
if final_battle == '1':
    delay_print(''+ player1name + ', you have chosen to battle Giovanni. Let the Final Battle begin!')
    print()
elif final_battle == '2':
    delay_print(''+ player1name + ', you have chosen to battle Brock. Let the Final Battle begin!')
    print()
elif final_battle == '3':
    delay_print(''+ player1name + ', you have chosen to battle Misty. Let the Final Battle begin!')
    print()

# Fighting Dojo Final Battle input
def battle_5():
    # Rival: Gym Leader
    opponent_team = [6, 10, 18, 24, 30, 36, 42, 61, 35, 47, 66, 64, 75, 76, 99, 96, 150]
    opponent_choice = random.choice(opponent_team)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(opponent_choice)

    response = requests.get(url)
    pokemon = response.json()

    opponent_poke = pokemon["name"]
    opponent_poke_xp = pokemon["base_experience"]
    opponent_poke_weight = pokemon["weight"]
    opponent_poke_height = pokemon["height"]

    delay_print("The Gym Leader, has chosen to attack with {}. ".format(opponent_poke))
    #delay_print_pokemon("{}".format(opponent_choice))
    print()
    #Player
    print()
    player_choice = input("Which Pokémon do you want to attack with? " "\n""{}".format(player_party))

    print()
    delay_print("You have chosen to attack with {}.".format(player_choice))
    #delay_print_pokemon("{}".format(player_choice))
    print()

    delay_print("Your chosen Pokémon {} has the following attributes: ".format(player_choice))

    print()
    print("╭──────────────────────────────╮")
    print("|                              |")
    print("            {}                  ".format(player_choice.capitalize()))
    print("|                              |")
    print("╰──────────────────────────────╯")

    #Level 2 attributes - edit!

    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(player_choice)

    response = requests.get(url)
    pokemon = response.json()

    player_poke_xp_3 = pokemon["base_experience"] + 50
    player_poke_weight_3 = pokemon["weight"] + 50
    player_poke_height_3 = pokemon["height"] + 50

    print("╭──────────────────────────────╮")
    print("|                              |")
    delay_print(" ---> [1] XP: {}".format(player_poke_xp_3)+"\n")
    delay_print(" ---> [2] Height: {}".format(player_poke_height_3)+"\n")
    delay_print(" ---> [3] Weight: {}".format(player_poke_weight_3)+"\n")
    print("|                              |")
    print("╰──────────────────────────────╯")
    print()

    player_attack = input("Which attribute do you want to use in battle (1/2/3)? ")

    if player_attack == "1":
        if player_poke_xp_3 > opponent_poke_xp:
            delay_print("Your Pokémon XP is {}. The Gym Leader's Pokémon XP is {}. You WIN! The attributes of all Pokémon in your party have increased by 10 points.".format(player_poke_xp_3, opponent_poke_xp))
            print() # Won the battle & the game
            print()
            delay_print('Congratulations, you have defeated the Final Gym Leader! You are now a Pokémon master. Collect your medal.')
            print()
            print()
            print(' _______________        ')
            print('|@@@@|     |####|       ')
            print('|@@@@|     |####|       ')
            print('|@@@@|     |####|       ')
            print('\@@@@|     |####/       ')
            print( '\@@@|     |###/        ')
            print('  `@@|_____|##          ')
            print('       (O)              ')
            print('    .-     -.           ')
            print('  .   * * *  `.         ')
            print(' :  *       *  :        ')
            print(':  ~ Pokémon ~  :       ')
            print(':  ~ MASTER ~   :       ')
            print(' :  *       *  :        ')
            print('  `.  * * *  .          ')
            print('    `-.....-            ')
            print()
            exit()
        else:
            delay_print("Your Pokémon XP is {}. The Gym Leader's Pokémon XP is {}. You LOSE! ".format(player_poke_xp_3, opponent_poke_xp))
            print()
            want_to_continue = input('Do you want to try this battle again? (y/n) ' .lower()) 

            if want_to_continue.lower() == 'y':
              delay_print("{}, let’s try this battle again!".format(player1name))
              print()
              battle_3()
            else:
              delay_print("{}, you have not won this battle.".format(player1name))
              print() # Game over
              print()
              print('_______  _______  __   __  _______    _______  __   __     _______  ______    ')  
              print('|       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  ')
              print('|    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  ')
              print('|   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ ')
              print('|   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |')
              print('|   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |')
              print('|_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|')
              print()
              exit ()
            time.sleep(1)
            
    if player_attack == "2":
        if player_poke_height_3 > opponent_poke_height:
            delay_print("Your Pokémon height is {}. The Gym Leader's Pokémon height is {}. You WIN! The attributes of all Pokémon in your party have increased by 10 points.".format(player_poke_height_3, opponent_poke_height))
            print() # Won the battle & the game
            print()
            delay_print('Congratulations, you have defeated the Final Gym Leader! You are now a Pokémon master. Collect your medal.')
            print()
            print()
            print(' _______________        ')
            print('|@@@@|     |####|       ')
            print('|@@@@|     |####|       ')
            print('|@@@@|     |####|       ')
            print('\@@@@|     |####/       ')
            print( '\@@@|     |###/        ')
            print('  `@@|_____|##          ')
            print('       (O)              ')
            print('    .-     -.           ')
            print('  .   * * *  `.         ')
            print(' :  *       *  :        ')
            print(':  ~ Pokémon ~  :       ')
            print(':  ~ MASTER ~   :       ')
            print(' :  *       *  :        ')
            print('  `.  * * *  .          ')
            print('    `-.....-            ')
            print()
            exit()
        else:
            delay_print(
                "Your Pokémon height is {}. The Gym Leader's Pokémon height is {}. You LOSE!".format(player_poke_height_3, opponent_poke_height))
            print()
            want_to_continue = input('Do you want to try this battle again? (y/n) ' .lower()) 

            if want_to_continue.lower() == 'y':
              delay_print("{}, let’s try this battle again!".format(player1name))
              print()
              battle_3()
            else:
              delay_print("{}, you have not won this battle.".format(player1name))
              print() # Game over
              print()
              print('_______  _______  __   __  _______    _______  __   __     _______  ______    ')  
              print('|       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  ')
              print('|    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  ')
              print('|   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ ')
              print('|   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |')
              print('|   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |')
              print('|_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|')
              print()
              exit ()
            time.sleep(1)
            
    if player_attack == "3":
        if player_poke_weight_3 > opponent_poke_weight:
            delay_print("Your Pokémon weight is {}. The Gym Leader's Pokémon weight is {}. You WIN! The attributes of all Pokémon in your party have increased by 10 points.".format(player_poke_weight_3, opponent_poke_weight))
            print() # Won the battle & the game
            print()
            delay_print('Congratulations, you have defeated the Final Gym Leader! You are now a Pokémon master. Collect your medal.')
            print()
            print()
            print(' _______________        ')
            print('|@@@@|     |####|       ')
            print('|@@@@|     |####|       ')
            print('|@@@@|     |####|       ')
            print('\@@@@|     |####/       ')
            print( '\@@@|     |###/        ')
            print('  `@@|_____|##          ')
            print('       (O)              ')
            print('    .-     -.           ')
            print('  .   * * *  `.         ')
            print(' :  *       *  :        ')
            print(':  ~ Pokémon ~  :       ')
            print(':  ~ MASTER ~   :       ')
            print(' :  *       *  :        ')
            print('  `.  * * *  .          ')
            print('    `-.....-            ')
            print()
            exit()
        else:
            delay_print(
                "Your Pokémon weight is {}. The Gym Leader's Pokémon weight is {}. You LOSE!".format(player_poke_weight_3, opponent_poke_weight))
            print()
            want_to_continue = input('Do you want to try this battle again? (y/n) '.lower()) 

            if want_to_continue.lower() == 'y':
              delay_print("{}, let’s try this battle again!".format(player1name))
              print()
              battle_3()
            else:
              delay_print("{}, you have not won this battle.".format(player1name))
              print() # Game over
              print()
              print('_______  _______  __   __  _______    _______  __   __     _______  ______    ')  
              print('|       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  ')
              print('|    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  ')
              print('|   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ ')
              print('|   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |')
              print('|   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |')
              print('|_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|')
              print()
              exit ()
            time.sleep(1)
battle_5()
delay_print("Congratluations {}, you have finished the game.".format(player1name))
sys.exit(0)