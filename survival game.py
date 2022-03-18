import sys
import random
import time

print("\033[1;31m\nWelcome to Lost without Recollection \033[0;0m")
print("""
                                                    \033[1;30;47m____\033[0;0m
                                         v        \033[1;30;47m _(    )\033[0;0m
         \033[1;32m_ ^ _ \033[0;0m                         v         \033[1;30;47m (___(__)\033[0;0m
        \033[1;32m'_\V/ `\033[0;0m
        \033[1;32m' oX`\033[0;0m
         \033[1;32m X\033[0;0m                            v
          \033[1;33mX\033[0;0m             -HELP!
          \033[1;33mX\033[0;0m                                                 
          \033[1;33mX\033[0;0m        \O/                                      
         \033[1;33m X.a##a.\033[0;0m   m                                     
       \033[1;33m.aa########a.\033[0;0m>>                                    
    \033[1;33m.a################aa.\033[0;0m                                 
\033[1;34m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0;0m""")
user = input("\nEnter Name: ")


def intro():
    print(
        "\n\033[1;32mYou wake up with amnesia, and a bit of a headache... \033[0;0m")
    print()
    print("\033[1;32mWere you thrown overboard? In a crash? A party on a yacht ?  Maybe pirates made you walk the plank. It doesnt matter. You are stranded \033[0;0m")
    print("\033[1;32mThere are no signs of a ship or a wreck or people. Just you, on your jack jones, dying of thirst, starving, and wondering how you got here.... And more importantly....how to get back to the warm security of civilisation....\033[0;0m")
    print()
    print(
        f"\033[1;32m{user} is confused and needs to make a decision\033[0;0m")
    print(
        "\033[1;32mThere is sea, a beach and a forest.....what do you do ?\033[0;0m")

    print(
        f"\033[1;32mWhether to stay on the beach where you woke up, head into the jungle or go round to the Far Side....\033[0;0m")
    answer_1 = input(
        "\nEnter 1 for Beach, 2 for Jungle or 3 to visit the far side of the island: ")
    if answer_1 == "1":
        print(f"\n\033[1;32mYou head toward the beach\033[0;0m")
        print(
            f"\033[1;32mand see a faint outline near the shore\033[0;0m")
        print(
            f"\033[1;32mDo you scout the beach or head towards the shore\033[0;0m")
        beach()
    elif answer_1 == "2":
        print(f"\033[1;32m\nYou head into the jungle\033[0;0m")
        jungle()
    elif answer_1 == "3":
        print(
            f"\n\033[1;32mYou head to the far side of the island.\033[0;0m")
        far_side()
    else:
        intro()


def beach():
    print(" ")
    print("\033[1;32mTo either scout the beach or head to the shore\033[0;0m")
    answer_2 = input(
        "\nEnter 1 to scout the beach or 2 to head towards the shore: \033[0;0m")
    if answer_2 == "1":
        print(f"\n\033[1;32m{user} decides to scout the beach\033[0;0m")
        fire_tiger_end()
    elif answer_2 == "2":
        print(f"\n\033[1;32m{user} heads towards the shore\033[0;0m")
        shore()
    else:
        beach()


def jungle():
    print("")
    print(
        f"\033[1;32mYou can hear the roar of animals yet can see fruit and berries in the distance\033[0;0m")
    print(
        f"\033[1;32mShould {user} look for shelter in a cave or collect food\n\033[0;0m")
    answer_3 = input("Enter 1 to find a cave or 2 to collect food: \033[0;0m")
    if answer_3 == "1":
        print(
            f"\033[1;32m\n{user} searches for shelter and finds a cave nearby\033[0;0m")
        cave_bear_end()
    elif answer_3 == "2":
        print(
            f"\033[1;32m\n{user} feels hungry and decides to look for food\n\033[0;0m")
        berry_mush_end()
    else:
        jungle()


def shore():
    print(" ")
    print(
        f"\033[1;32mClose to the shore, {user} see a cabin and a pier\033[0;0m")
    print(f"\033[1;32mShould you go to the cabin or the pier\033[0;0m")
    answer_4 = input("\nEnter 1 for Cabin and 2 for Pier: ")
    if answer_4 == "1":
        print(f"\n\033[1;32m{user} sets off towards the cabin\033[0;0m")
        escape()
    elif answer_4 == "2":
        print(f"\n\033[1;32m{user} heads towards the pier\033[0;0m")
        pier()
    else:
        shore()


def escape():
    print(f"\n\033[1;35mClose to the shore, you sees a cabin\033[0;0m")
    print(f"\033[1;35mIn the cabin you find a flare gun\033[0;0m")
    print(
        f"\033[1;35mBetter check to see if the flare gun is operational...Yes!\033[0;0m")
    print(
        f"\033[1;35mThen {user} hears some sort of engine from across the sea\033[0;0m")
    print(
        f"\033[1;35mUpon hearing this, you jump out of the cabin and bolt towards the shore\033[0;0m")
    print(
        f"\033[1;35mOnce you reach the shore, you fire the flaregun in order to get the passing boats attention\033[0;0m")
    print(
        "\033[1;35mThe boat starts to slow down once the flare has been shot\033[0;0m")
    print("\033[1;35mIt starts to approach the shore\033[0;0m")
    print(
        f"\033[1;35mOnce it has reached the shore, {user} explains their situation to the crew \033[0;0m")
    print("\033[1;35mThey agree to drop you of at the nearest port\033[0;0m")
    print(" ")
    print("                                         YOU ESCAPE !")
    print("Will you piece together the events that got there in the first place? Find out in our sequel !")

    game_over_escape = input(
        f"\n{user}, press 1 to Play again, or 2 to end game: ")

    if game_over_escape == "1":
        intro()
    elif game_over_escape == "2":
        end()
    else:
        escape()


def pier():
    print(" ")

    print(
        f"\n\033[1;31m{user}reaches the pier and sees a box with fishing rods in it \033[0;0m")
    print(
        f"\033[1;31mAs you go to the box to inspect the contents....\033[0;0m")
    print(
        f"\033[1;31mA huge Jellyfish jumps out and latches itself onto you\033[0;0m")
    print(
        f"\033[1;31mYou struggle in vain to get it off and are shocked half to death as a result\033[0;0m")
    print(" ")

    print(
        f"\033[1;31mLaying motionless, you wonder what you did in life for it to end like this\033[0;0m")

    game_over_pier = input(
        f"\n{user}, press 1 to Play again, or 2 to end game: ")

    if game_over_pier == "1":
        intro()
    elif game_over_pier == "2":
        end()
    else:
        pier()


def cave_bear_end():
    print(
        "\033[1;32mThere is a fur pelt and a large stick at the entrance. \033[0;0m")
    print(
        f"\033[1;32mYou look around to see if there is anything else\033[0;0m")
    print(
        f"\033[1;32mUpon further inspection you could not find anything more useful\033[0;0m")
    print(
        f"\033[1;32m{user} wondered if anyone else had ended in his predicament...\033[0;0m")
    print(f"\033[1;32mWhat shall {user} choose?\n\033[0;0m")
    answer_1 = input("Enter 1 for pelt or 2 for stick: ")
    if answer_1 == "1":
        pelt()
    elif answer_1 == "2":
        stick()
    else:
        cave_bear_end()


def pelt():
    print(
        f"\033[1;34m\n{user} decides to put on the pelt as it becomes a bit cooler\033[0;0m")
    print(
        f"\033[1;34mAfter wearing the animal pelt you leave the cave and look for a sturdy tree\033[0;0m")
    print("  ")
    print(f"\033[1;34mYou find a tree, climb it and sleep in it to avoid any hungry animals that may try to eat you while snoozing\033[0;0m")
    print(" ")
    print(
        f"\033[1;34mAfter a few hours of rest you are awoken by the sound of a ships engine\033[0;0m")
    print(f"\033[1;34mYou just realise... You have missed a chance at attaining freedom from this place. You ponder whether another will come to save you....\033[0;0m")
    game_over_pelt = input(
        f"\n{user}, press 1 to Play again, or 2 to end game: ")

    if game_over_pelt == "1":
        intro()
    elif game_over_pelt == "2":
        end()
    else:
        pelt()


def stick():
    print(
        f"\n\033[1;31mYou pick up the stick, and begin to feel adventurous. You decide to head further into the cave\033[0;0m")
    print(f"\033[1;31mYou delve further into the cave... On feeling a cold shiver, you merely pass it of as feeling cold. Maybe you should go back for the pelt...\033[0;0m")
    print("  ")
    print(
        f"\033[1;31mThe deeper into the the cave the less the light, until {user} bumps into some sort of mound and flesh\033[0;0m")
    print(
        f"\033[1;31mA lump develops in the back of your throat as the lump of fur and flesh moves, it is a.... hibernating bear ! And not happy to be woken up\033[0;0m")
    print(f"\033[1;31mEven though you have some sort of weapon and scream at the top of your lungs, it pales in comparison to the raw natural power of the irate bear\033[0;0m")
    print("  ")
    print(
        f"\033[1;31mAs you lay there motionless, the bear leaves you and decides to return to its slumber once more\033[0;0m")
    print(
        f"\033[1;31m{user}s broken body is left for the other cave critters and creatures to feast upon\033[0;0m")
    game_over_stick = input(
        f"\n{user}, press 1 to Play again, or 2 to end game: ")

    if game_over_stick == "1":
        intro()
    elif game_over_stick == "2":
        end()
    else:
        stick()


def berry_mush_end():
    print("\033[1;32mYou go in search of food. You find berries and mushrooms.\nWhich do you eat?\n\033[0;0m")
    answer_1 = input("Enter 1 for Berries or 2 for Mushrooms: ")
    if answer_1 == "1":
        berry()
    elif answer_1 == "2":
        mush()
    else:
        berry_mush_end()


def berry():
    print(f"\n\033[1;35mYou climb a tree to reach for fruits and berries, pick as much as possible, then descend from the tree.\033[0;0")
    print(f"\033[1;35mOn the way down you slip and fall. Fortunately you and the fruits land in the bushes, but cut your arm on some thorns.\033[0;0")
    print("  ")
    print(
        f"\033[1;35mAfter wrapping your arm in leaves, you eats a filling amount of fruit and go to sleep exhausted.\033[0;0")
    print(
        f"\033[1;35mYou wake up the next day to the clear sound of a boat horn.\033[0;0")
    print("  ")
    print(
        f"\033[1;35mRushing back down to the beach you shout for help, whilst throwing anything in reach... amazingly the crew see you and come to {user}'s rescue.\nWELL DONE!.\033[0;0m")

    game_over_berry = input(
        f"\n{user}, press 1 to Play again, or 2 to end game: ")

    if game_over_berry == "1":
        intro()
    elif game_over_berry == "2":
        end()
    else:
        berry()


def mush():
    print(
        f"\n\033[1;31mThe fruit and berries are high in the trees... you decide not to risk breaking a bone by falling, and pick a mushroom.\n \nThey look normal enough so you takes a bite. The mushrooms taste ok, only you wish you had a fire to cook them on.\nUnfortunately {user}, the tasty looking fungi are poisonous and after some time you start to feel nauseous.\n \nYou start to vomit uncontrollably and the hallucinations set in...\nyou think you hear a boat in the distance but who knows...\n \nEventually, you pass out and die from dehydration in your sleep.\n \nGAME OVER!\033[0;0m")

    game_over_mush = input(
        f"\n{user}, press 1 to Play again, or 2 to end game: ")

    if game_over_mush == "1":
        intro()
    elif game_over_mush == "2":
        end()
    else:
        mush()


def fire_tiger_end():
    print("\033[1;32mYou go on a scouting mission, and come across some burning embers, a fire from hours before. Humans are here!. \033[0;0m")
    print(
        "\033[1;32mShould you stay around the fire, or continue on your recce.... . \033[0;0m")
    print("\033[1;32mWhat do you choose?\033[0;0m\n")
    answer_1 = input(
        "Enter 1 to stay and rekindle the fire or 2 to keep roaming: ")
    if answer_1 == "1":
        rekindle()
    elif answer_1 == "2":
        recce()
    else:
        fire_tiger_end()


def rekindle():
    print(
        f"\n\033[1;31mYou rekindle the flames, hoping for some warmth, luckily it works and you fall asleep.\033[0;0m")
    print(
        f"\033[1;31mBut - you're rudely awakened from a deep slumber by the roar of a ravenous tiger.\033[0;0m")
    print(" ")
    print(
        f"\033[1;31mYou freak out and panic, tripping into the fire whilst the tiger stalks its prey \033[0;0m")
    print(
        f"\033[1;31m{user}.... Thinking to self..... No wonder the fire was abandoned\033[0;0m")
    print(" ")
    print(
        f"\033[1;31mIn a flash the tiger pounces and with its huge sharp front teeth it tears through your torso like it was paper...\nGAME OVER!.\033[0;0m")
    game_over_rekindle = input(
        f"\n{user}, press 1 to Play again, or 2 to end game: ")

    if game_over_rekindle == "1":
        intro()
    elif game_over_rekindle == "2":
        end()
    else:
        rekindle()


def recce():
    print(
        f"\n\033[1;31mYou ignore the the embers of a fire from another time and keep wandering\033[0;0m")
    print(f"\033[1;31mJust before you pass the fire, a gust of wind blasts the ember filled wood across your face.\nIt ends with a massive cut stretching from the ear to the corner of your mouth\033[0;0m")
    print("  ")
    print(f"\033[1;31mNight begins to fall and you have no shelter or warmth.\nTiredness sets in and you begin to get drowsy and just knock out on the beach\033[0;0m")
    print(f"\033[1;31m{user} is fast asleep on the beach, however due to the plummeting night temperature to negative 10 you die of hypothermia. \nGAME OVER!\033[0;0m")

    game_over_recce = input(
        f"\n{user}, press 1 to Play again, or 2 to end game: ")

    if game_over_recce == "1":
        intro()
    elif game_over_recce == "2":
        end()
    else:
        recce()


# ---Additional route--

# Global variable hunger. User starts with 99 points (full hunger percentage) minus a random amount between 15 and 30. Drop below 0 points and the user dies of starvation. This varaible only applicable to the far side of the island "far_side()"". Each decision event takes time (eg, travel to another location), therefore the user looses hunger points.
hunger = 99

#  -------Start Hunger section-------

# This function is called by each decision event (by decision event I mean something such as go to sand dunes, go to forest, etc).


def hunger_if():
    global hunger
    global user

    # This ensures the hunger level is never above 99.
    if hunger > 100:
        hunger = 99

    # This IF statement determines the message presented to the user, informing them of their hunger level. If hunger drops below 0, the game_over_starved function is called.

    # If hunger level number is between the bounds of (lower number) and (upper number), then print its corresponding message.
    if hunger in range(0, 15):
        print(
            f"\n{user}, you have almost starved to death. Your \033[1;36;40mhunger\033[0;0m level is \033[1;31;40m{hunger}%\033[0;0m.\n")  # hunger points number turns red when this low.
    elif hunger in range(15, 25):
        print(
            f"\n{user}, you are famished. Your \033[1;36;40mhunger\033[0;0m level is \033[1;31;40m{hunger}%\033[0;0m.\n")  # hunger points number turns red when this low.
    elif hunger in range(25, 35):
        print(
            f"\n{user}, you are peckish. Your \033[1;36;40mhunger\033[0;0m level is \033[1;32;40m{hunger}%\033[0;0m.\n")  # hunger points number is green from this amount of points and up.
    elif hunger in range(35, 50):
        print(
            f"\n{user}, you are somewhat satiated. Your \033[1;36;40mhunger\033[0;0m level is \033[1;32;40m{hunger}%\033[0;0m.\n")
    elif hunger in range(50, 65):
        print(
            f"\n{user}, you are satiated. Your \033[1;36;40mhunger\033[0;0m level is \033[1;32;40m{hunger}%\033[0;0m.\n")
    elif hunger in range(65, 85):
        print(
            f"\n{user}, you are feeling quite full. Your \033[1;36;40mhunger\033[0;0m level is \033[1;32;40m{hunger}%\033[0;0m.\n")
    elif hunger in range(85, 999):
        print(
            f"\n{user}, you are feeling very full. Your \033[1;36;40mhunger\033[0;0m level is \033[1;32;40m{hunger}%\033[0;0m.\n")
    # if hunger level number is below 0. Then call the game_over_starved function. This ends the game.
    if hunger < 0:
        print(
            "\nYour \033[1;36;40mhunger\033[0;0m level dropped below \033[1;31;40m0%\033[0;0m.\n")
        game_over_starved()


# global_vars_minus_hunger obtains hunger level. Reduces hunger level by a random amount between 15 and 30. Then calls the hunger IF statment function, to either print the correct message for the users current hunger level, or to end the game because the hunger level has dropped below 0.
def global_vars_minus_hunger():
    global hunger
    hunger -= random.randint(15, 30)
    hunger_if()

# global_vars_plus_hunger obtains hunger level. Increases hunger level by a random amount between 15 and 30. Then calls the hunger IF statment function.


def global_vars_plus_hunger():
    global hunger
    hunger += random.randint(30, 60)
    hunger_if()

 
# game_over_starved function is called by the hunger_if function if hunger drops below 0. This ends the game, and gives the user an option to start again.
def game_over_starved():
    print(
        f"\nSomewhat unfortunatly, you have died of starvation. Did you not stop to think how much paperwork we would have to do in the event of your death? Rather selfish of you {user}.\nAnyway it was nice knowing you {user}.")
    game_over_replay = input(
        "\n1: Return to the beach.\n2: End game.\n\nChoice: ")

    if game_over_replay == "1":
        intro()
    elif game_over_replay == "2":
        end()
    else:
        game_over_starved()

#  -------End Hunger section-------


def far_side():
    global hunger
    # This ensures the user starts intro with 99 points. This line is required if this section of the game is replayed after dying/finishing.
    hunger = 99

    print(f"\nWelcome {user} to the far side of the island, you are a most welcome guest to our section of our little island paradise.\n\nThis section of the island is teeming with deadly dangerous animals such as tigers, bears, Jack Russells and highly venomous snakes.\nWe advise you to avoid the locals... apparently they are cannibals, but they really are lovely people otherwise. Atleast the weather is nice?")

    print(
        f"\nPlease be aware that each decision you make on the far side of the island takes time to enact, which means you get hungrier and become famished, unless you make some decisions which award you food?\n\nIf your hunger drops below \033[1;31;40m0%\033[0;0m, you will starve to death.\n\nThe governor would like to advise all inmates...erm I mean guests, that it would be most irresponsible to starve to death,\npartly because dying due to starvation may prove detrimental to your quality of life and future life prospects, but mainly because the island's liability insurance does not cover starvation\nunder subsection D of article 12 of the penal code. \x1B[3mAnyway, enjoy your stay {user}!\x1B[0m")
    far_side_landing()


def far_side_landing():
    # global_vars_minus_hunger removes a random amount of hunger points between 15-30 points.
    global_vars_minus_hunger()
    far_side_start()


def far_side_start():
    # global_vars_minus_hunger removes a random amount of hunger points between 15-30 points.

    print(f"\n{user}, you are on the far side of the island. ")
    far_side_start_q = input(
        "\n1: Explore the sand dunes. \n2: Explore the forest.\n3: Visit the lake.\n4: Go back to the main beach.\n\nChoice: ")

    # Calls the dunes_1_landing function to explore the beach.
    if far_side_start_q == "1":
        dunes_1_landing()

    # Calls the forest_1_landing function to go into the forest.
    elif far_side_start_q == "2":
        forest_1_landing()

    # Calls the lake_1_landing function to go into the lake.
    elif far_side_start_q == "3":
        lake_1_landing()

    # Sends the user back to the main beach.
    elif far_side_start_q == "4":
        intro()

    # Any other input than 1 or 2 causes this function to repeat.
    else:
        far_side_start()


# dunes_1_landing is the landing screen for going to the sand dunes. This in turn will call the dunes_1 function, which is a decision event function.
def dunes_1_landing():
    # global_vars_minus_hunger removes a random amount of hunger points between 15-30 points.
    global_vars_minus_hunger()
    dunes_1()


def dunes_1():
    global hunger
    print(
        f"\nWelcome to the sand dunes {user}.\n\nThere appears to be a shipwreck in the sand dunes, don't ask us how it got here, we really do request all guests to please take their unwanted items home with them.\nIn the distance you spot some very friendly locals cooking on a very large campfire, complete with a spit roast.\nThey appear to be shouting and gesturing at you to join them for a hearty meal as a guest of honour, perhaps you could get something to eat?")
    print("\nWould you like to explore the shipwreck, or enjoy a hearty meal?")
    dunes_1_q = input(
        "\n1: Explore shipwreck.\n2: Enjoy a hearty meal.\n3: Return to the far side of the island.\n\nChoice: ")

    if dunes_1_q == "1":
        shipwreck_1_landing()
    elif dunes_1_q == "2":
        meal_1_landing()
    elif dunes_1_q == "3":
        far_side_landing()
    else:
        dunes_1()
    # The dunes is split into dunes_1_landing and dunes_1. If they were combined in the same function and if somebody was to type any other input than 1 or 2, then global_vars_minus_hunger() would be enacted repeatedly for each failed input attempt (because of the 'else' condition being met). So the user would rapidly die due to hunger points dropping below 0.


def shipwreck_1_landing():
    # global_vars_minus_hunger removes a random amount of hunger points between 15-30 points.
    global_vars_minus_hunger()
    shipwreck_1()


def shipwreck_1():
    global hunger
    print(
        f"\nWelcome to the shipwreck {user}.\n\nYou have stumbled upon a treasure chest.")
    print("\nWould you like to open the treasure chest or return to the sand dunes?")
    shipwreck_1_q = input(
        "\n1: Open treasure chest.\n2: Return to the sand dunes.\n\nChoice: ")

    if shipwreck_1_q == "1":
        treasure_1_landing()
    elif shipwreck_1_q == "2":
        dunes_1_landing()
    else:
        shipwreck_1()


def treasure_1_landing():
    global_vars_plus_hunger()
    treasure_1()


def treasure_1():
    global hunger
    print(
        f"\nYou opened the treasure chest {user}. It seems some very friendly locals recently stored some cooked meat in the chest.\nYou found it to have a quite distinct and unfamiliar taste, but it did the job and restored your \033[1;36;40mhunger\033[0;0m level to \033[1;32;40m{hunger}%\033[0;0m.")
    treasure_1_q = input(
        "\nPress 1 to return to the sand dunes.\n\nChoice: ")
    if treasure_1_q == "1":
        dunes_1_landing()
    else:
        treasure_1()


def meal_1_landing():
    print(
        f"\n{user}, there appears to have been a slight misunderstanding. You were not to be the guest of honour for the meal, you were to be the meal for a guest of honour.\nWe apologise for any inconvenience caused to you by your death.\n\nIf its any consolation {user}, the locals were most content with their meal, a little bit too much gristle perhaps, but an otherwise most delicious meal.\nMost curiously, the guest of honour was a Jack Russell. The locals appeared to be afraid of her.")
    meal_1_q = input(
        "\n1: Return to the beach.\n2: End game.\n\nChoice: ")
    if meal_1_q == "1":
        intro()
    elif meal_1_q == "2":
        end()
    else:
        meal_1_landing()


def forest_1_landing():
    # global_vars_minus_hunger removes a random amount of hunger points between 15-30 points.
    global_vars_minus_hunger()
    forest_1()


def forest_1():
    global hunger
    print(
        f"\nWelcome to the forest {user}.\n\nTo your left you notice some strange objects in the undergrowth, perhaps these are worth investigating?\nTo your right, you spot a small furry animal in the bushes, you are an animal person aren't you?")
    forest_1_q = input(
        "\n1: Search the undergrowth.\n2: Approach the presumably friendly furry animal.\n3: Return to the far side of the island.\n\nChoice: ")

    if forest_1_q == "1":
        undergrowth_1_landing()
    elif forest_1_q == "2":
        animal_1_landing()
    elif forest_1_q == "3":
        far_side_landing()
    else:
        forest_1()


def undergrowth_1_landing():
    global_vars_plus_hunger()
    undergrowth_1()


def undergrowth_1():
    global hunger
    print(
        f"\nYou searched the undergrowth, found and ate some sort of dinosaur eggs? And subsequently replenished your \033[1;36;40mhunger\033[0;0m level to \033[1;32;40m{hunger}%\033[0;0m.\nThey were bright purple and tasted revolting, but they seemed to do the job...Personally I would have just eaten that Twix you forgot about in your back pocket.")
    undergrowth_1_q = input(
        "\nPress 1 to return to the forest.\n\nChoice: ")
    if undergrowth_1_q == "1":
        forest_1_landing()
    else:
        undergrowth_1()


def animal_1_landing():
    print(
        f"\nUnfortunatly {user}, you were mauled to death and eaten by a rather mild tempered Jack Russell (mild by Jack Russell standards).\nWe did try to warn you of these deadly vicious creatures.\n\nIf its any consolation {user}, the Jack Russell was most content with her meal, a little bit too much gristle perhaps, but an otherwise most delicious meal.")
    meal_1_q = input(
        "\n1: Return to the beach.\n2: End game.\n\nChoice: ")
    if meal_1_q == "1":
        intro()
    elif meal_1_q == "2":
        end()
    else:
        animal_1_landing()


def lake_1_landing():
    # global_vars_minus_hunger removes a random amount of hunger points between 15-30 points.
    global_vars_minus_hunger()
    lake_1()


def lake_1():
    global hunger
    print(
        f"\nWelcome to the lake {user}.\n\nHere you can catch some of the islands delicious fish.\nMost have 3 eyes and a couple of arms, but they are delicious nonetheless.\nYou have a one in three chance of catching a fish.")
    print("\nWould you like to take a chance on catching a fish?")
    lake_1_q = input(
        "\n1: Go fishing.\n2: Return to the far side of the island.\n\nChoice: ")

    if lake_1_q == "1":
        fish_1_landing()
    elif lake_1_q == "2":
        far_side_landing()
    else:
        lake_1()


def fish_1_landing():
    global_vars_minus_hunger()
    fish_1()


def fish_1():
    print(
        f"\nCast off {user}?")
    fish_1_q = input(
        "\n1: Cast off.\n2: Return to the lake.\n\nChoice: ")
    if fish_1_q == "1":
        fish_random()
    elif fish_1_q == "2":
        lake_1_landing()
    else:
        fish_1()


def fish_random():
    global hunger

    x = random.randint(0, 2)
    fish_random_number = random.randint(0, 7)

    # --- Random fish message lists ---

    # A list of outcomes. This gives us index numbers to call upon to get their contents.
    no_fish_list = [
        f"\nOh, bad luck {user}... You only caught an Aldi coupon book. They all appear to have expired, and you don't shop there anyway.",
        f"\nOh, bad luck {user}... You only caught a book titled: Jack Russells - Natures most deadly creatures.",
        f"\nOh, bad luck {user}... You only caught a novelty hat in the shape of a Jack Russell.",
        f"\nOh, bad luck {user}... You only caught a garden gnome.",
        f"\nOh, bad luck {user}... You only caught a hand made wooden figurine of a Jack Russell. Apparently the locals worship this creature.",
        f"\nOh, bad luck {user}... You only caught a Tesco shopping trolley.",
        f"\nOh, bad luck {user}... You did not catch a thing. You hear laughter emanating from the lake... the fish apparently found your attempt amusing.",
        f"\nOh, bad luck {user}... I bet you couldn't even catch a cold.",
    ]

    # no_fish = an object from the no_fish_list [with the index number chosen by fish_random_number]
    no_fish = (no_fish_list[fish_random_number])

    # A list of outcomes. This gives us index numbers to call upon to get their contents.
    caught_fish_list = [
        f"\n{user} has caught a fish! It pleads with you in English to throw it back into the lake, but you pretend you can only speak Spanish and ignore its pleas.",
        f"\n{user} has caught a fish! Apparently its name is Gerald...or was Gerald. You found Gerald to be most delicious.",
        f"\n{user} has caught a fish! It had three eyes and a couple of arms, but it was delicious nonetheless.",
        f"\n{user} has caught a fish! You eat it whole, arms and all.",
        f"\n{user} has caught a fish! It pleads with you in English to throw it back into the lake, but you pretend you can only speak Swahili and ignore its pleas.",
        f"\n{user} has caught a fish! It exclaims its royalty of this great lake, but you don't have time to hear such nonsense and devour it enthusiastically.",
        f"\n{user} has caught a fish! You develop a false sense of belief that you are actually quite good at this.",
        f"\n{user} has caught a fish! Well done {user}!",
    ]

    # caught_fish = an object from the caught_fish_list [with the index number chosen by fish_random_number]
    caught_fish = (caught_fish_list[fish_random_number])

    if x == 0:
        print(f"\n{user} casts off to the centre of the lake and waits patiently...")
        time.sleep(2)  # Sleep for 2 seconds
        print(no_fish)
        global_vars_minus_hunger()

    elif x == 1:
        print(
            f"\n{user} casts off to the centre of the lake and waits patiently....")
        time.sleep(2)
        print(no_fish)
        global_vars_minus_hunger()

    else:
        print(
            f"\n{user} casts off to the centre of the lake and waits patiently....")
        time.sleep(2)
        print(caught_fish)
        global_vars_plus_hunger()

    fish_1()


def end():
    print("Exiting Game")
    sys.exit()


intro()
