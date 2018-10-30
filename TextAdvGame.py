# File:    proj1.py
# Author:  Nathenael Dereb
# Description: Creating a text adventure game by
# utilizing while loops, control statements, if/else statements, passing in parameters,
# returning from functions, and shallow and deep copies of lists.

from random import randint

MILES_TO_SURVIVE = 150
DAYS_TO_SURVIVE = 7
wafflesHealthBoost = 10
MIN_HEALTH = 0
MAX_HEALTH = 100
DEMOG_MAX_HEALTH = 300
DEMOG_BASE_ATTACK = 20
END = 4
MIN_CHOICE = 1
REESES_POWER = -30
POP_ROCKS_POWER = -5
OVALTINE_POWER = 15
HEELYS_POWER = 1.25
BICYCLE_POWER = 1.5
WONDER_BREAD_POWER = 25
TWINKIES_POWER = 25
CHOICES = ["View Inventory", "View Current Stats", "Eat an Eggo Waffle",
           "Nothing else"]
BACKPACK_ITEMS = ["Reese's Pieces", "Pop Rocks", "Ovaltine", "Wonder Bread",
                 "Twinkies"]
ITEMS_IN_SHED = ["Sword", "Bicycle", "HI-C", "Heelys", "Walkman", "Laser Cannon"
                 ,"Rubber Band"]

# displayMenu(choices)
#     prints a list of elements in choices.
# Input: choices; a list of all the possible choices available
def displayMenu(choices):
    indexChoice = 0
    while indexChoice < len(choices):
        print(indexChoice + 1,"-",choices[indexChoice])
        indexChoice += 1

# equipOptions()
#     prints a list of elements in equipOptList.
#     Uses Boolean flag for input validation
# Output: optChosen; returns the choice the user has made
def equipOptions():
    equipOptList = ['Equip', 'Unquip', 'I changed my mind']
    index = 0
    while index < len(equipOptList):
        print(index + 1, "-", equipOptList[index])
        index += 1
    optChosen = int(input("Enter a choice: "))
    flag = False
    while not flag:
        flag = True
        if optChosen < MIN_CHOICE:
            print('Enter a valid Option')
            optChosen = int(input('Enter a choice: '))
            print()
            flag = False
        elif optChosen > len(equipOptList):
            print('Enter a valid Option')
            optChosen = int(input('Enter a choice: '))
            print()
            flag = False
    return optChosen

# fightOptions()
#     prints a list of elements in fightOptList.
#     Uses Boolean flag for input validation
# Output: optChosen; returns the choice the user has made
def fightOptions():
    fightOptList = ['Fight', 'Flail', 'Flee']
    index = 0
    while index < len(fightOptList):
        print(index + 1, "-", fightOptList[index])
        index += 1
    optChosen = int(input("Enter a choice: "))
    flag = False
    while not flag:
        flag = True
        if optChosen < MIN_CHOICE:
            print('Enter a valid Option')
            optChosen = int(input('Enter a choice: '))
            flag = False
        elif optChosen > len(fightOptList):
            print('Enter a valid Option')
            optChosen = int(input('Enter a choice: '))
            flag = False
    return optChosen

# eatOptions()
#     prints a list of elements in eatOptList.
#     Uses Boolean flag for input validation
# Output: optChosen; returns the choice the user has made
def eatOptions():
    eatOptList = ['eat it', 'put it back']
    index = 0
    while index < len(eatOptList):
        print(index + 1, "-", eatOptList[index])
        index += 1
    optChosen = int(input("Enter a choice: "))
    flag = False
    while not flag:
        flag = True
        if optChosen < MIN_CHOICE:
            print('Enter a valid Option')
            optChosen = int(input('Enter a choice: '))
            flag = False
        elif optChosen > len(eatOptList):
            print('Enter a valid Option')
            optChosen = int(input('Enter a choice: '))
            flag = False
    return optChosen

# chooseItem(inventory)
#     prints a list of elements in inventory.
#     Uses Boolean flag for input validation
# Input:  inventory; list of all items in inventory.
# Output: itemChosen; returns the choice the user has made
def chooseItem(inventory):
    index = 0
    print()
    while index < len(inventory):
        print(index + 1, "-", inventory[index])
        index += 1
    itemChosen = int(input('Enter a choice: '))
    flag = False
    while not flag:
        flag = True
        if itemChosen < MIN_CHOICE:
            print('Enter a valid Option')
            itemChosen = int(input('Enter a choice: '))
            flag = False
        elif itemChosen > len(inventory):
            print('Enter a valid Option')
            itemChosen = int(input('Enter a choice: '))
            flag = False
    return itemChosen

# getUserChoice(choices)
#     calls function displayMenu(choices)
#     asks the user to select a choice from a list of choices
#     continuously prompts the user until the choice is valid
#     a valid choice is one that is a valid index in the list
#     Uses Boolean flag for input validation
# Input: choices; a list of all the possible choices available
# Output: choice; the validated choice that the user made
def getUserChoice(choices):
    displayMenu(choices)
    choice = int(input('Enter a choice: '))
    flag = False
    while not flag and choice != END:
        flag = True
        if choice < MIN_CHOICE:
            print('Enter a valid Option')
            choice = int(input('Enter a choice: '))
            flag = False
        elif choice > len(CHOICES):
            print('Enter a valid Option')
            choice = int(input('Enter a choice: '))
            flag = False
    return choice

# calculateDailyTask(equippedItem, player_health, inventory, distSum, eaten)
#     If choice == 1
#     Uses Boolean flag for input validation
#     Calls Function getUserChoice(CHOICES)
#     Calls Function chooseItem(inventory)
#     Checks to See if item chosen is equippable or not
#     if choice == 2
#     prints out current Health, Distance Travelled and equpped item.
#     if choice == 3
#     Eats Ego Waffel for health boost each day
#     if choice == 4
#     ENDS Sinetal Loop with END
# Input: equippedItem, player_health, inventory, distSum, eaten;
# Output: equipHealth; list( equippedList, player_health, eaten )
def calculateDailyTask(equippedItem, player_health, inventory, distSum, eaten):
    inventory = inventory
    equippedList = equippedItem
    equipped = "".join(equippedItem)
    player_health = player_health
    index = 0
    flag = False
    while not flag:
        flag = True
        choice = getUserChoice(CHOICES)

        if choice == 1:
            print('\nInventory:', inventory)
            optChosen = equipOptions()
            if optChosen == 1:
                # Checks to see if there is an item already equipped.
                if len(equippedList) >= 1:
                    print("\nYou cannot equip two items\n")
                    flag = False
                if len(equippedList) < 1:
                    itemChosen = chooseItem(inventory)
                    itemChosen = inventory[itemChosen - 1]
                    #Checks if user has chosen unequippable items - Input
                    # Validation
                    while itemChosen == 'Heelys' or itemChosen == 'HI-C' or \
                        itemChosen == 'Heeleys' or itemChosen == "Bicycle" or \
                        itemChosen == 'Walkman':
                        print("\n",itemChosen, 'cannot be equipped. Please '
                                             'choose an equippable item!\n')
                        itemChosen = chooseItem(inventory)
                        itemChosen = inventory[itemChosen - 1]
                    equippedList.append(itemChosen)
                    equipped = "".join(equippedItem)
                    print("\nYou've equipped:", itemChosen)
                    print()
                    flag = False
            if optChosen == 2:
                # evaluates list to Unequip item
                if len(equippedList) >= 1:
                    print("\nYou've unequipped your item:", equipped)
                    equippedList.remove(equippedList[index])
                    print()
                    flag = False
                # evaluates list to check if there is an item equipped
                elif len(equippedList) < 1:
                    print("\nYou have no equipped item\n")
                    flag = False
            if optChosen == 3:
                print("\nOK, that's fine.\n")
                flag = False

        if choice == 2:
            # prints  player health, distance travelled, and equipped item.
            equipped = "".join(equippedItem)
            if equipped == '':
                equipped = 'N/A'
            print('Player health:', player_health)
            print('Distance travelled:', distSum)
            print('Item equipped:', equipped)
            print('\n')
            flag = False

        if choice == 3:
            # Uses boolean flag to evaluate if Ego Waffle is eaten or not.
            if eaten:
                print('\nYou can only eat an Eggo Waffle once a day\n')
            if not eaten:
                eaten = True
                if eaten == True:
                    if player_health == MAX_HEALTH:
                        print('\nPlayer health is at maximum:', player_health)
                        print('')
                    if player_health < MAX_HEALTH:
                        print('\nYou ate the Eggo Waffle. So bad, yet so good. '
                              '\nYour health has increased by 10 points.\n')
                        player_health = player_health + wafflesHealthBoost
                        eaten = True
                    if player_health > MAX_HEALTH:
                        player_health = MAX_HEALTH
                        eaten = True
            flag = False
    equipHealth = []
    equipHealth.append(equippedList)
    equipHealth.append(player_health)
    equipHealth.append(eaten)
    return equipHealth

# travelledDist(player_health):
#     calculates distance travelled by player
#     updates distance travelled by player
#     returns distance_travelled by player
# Input: player_health; current health of player.
# Output: distance_travelled; current distance travelled by player
def travelledDist(player_health):
    distTravelled = (player_health / 4) + 5
    return distTravelled

# calcDamage(item):
#     calculates the amount of damage each item possesses.
#     returns damage
# Input: item; current item equipped by player.
# Output: damage; integer of damage the item causes
def calcDamage(item):
    if item == 'Flashlight':
        damage = 5
        return damage
    elif item == 'Walkie Talkie':
        damage = 10
        return damage
    elif item == 'Rubber Band':
        damage = 25
        return damage
    elif item == 'Sword':
        damage = 50
        return damage
    elif item == 'Laser Cannon':
        damage = 100
        return damage

# eat(food, player_health):
#     if food is in BACKPACK_ITEMS - Validation
#     updates player health depending on the food they eat
#     returns player_health
# Input: food, player_health; current health of player, and food eaten by player
# Output: player_health; current health of player
def eat(food, player_health):
    if food in BACKPACK_ITEMS:
        if food == "Reese's Pieces":
            if player_health < MAX_HEALTH:
                player_health += REESES_POWER
                print("\nYou're health has decreased:", REESES_POWER)
            if player_health >= MAX_HEALTH:
                player_health = MAX_HEALTH
            print('Player Health:', player_health)
        elif food == 'Pop Rocks':
            if player_health < MAX_HEALTH:
                player_health += POP_ROCKS_POWER
                print("\nYou're health has decreased by:", POP_ROCKS_POWER)
            if player_health >= MAX_HEALTH:
                player_health = MIN_HEALTH
            print('Player Health:', player_health)
        elif food == 'Ovaltine':
            if player_health < MAX_HEALTH:
                player_health += OVALTINE_POWER
                print("\nYou're health has increased by:",OVALTINE_POWER)
            if player_health >= MAX_HEALTH:
                player_health = MAX_HEALTH
            print('Player Health:', player_health)
        elif food == 'Wonder Bread':
            if player_health < MAX_HEALTH:
                player_health += WONDER_BREAD_POWER
                print("\nYou're health has increased by:", WONDER_BREAD_POWER)
            if player_health >= MAX_HEALTH:
                player_health = MAX_HEALTH
            print('Player Health:', player_health)
        elif food == 'Twinkies':
            if player_health < MAX_HEALTH:
                player_health += TWINKIES_POWER
                print("\nYou're health has increased by:", TWINKIES_POWER)
            if player_health >= MAX_HEALTH:
                player_health = MAX_HEALTH
            print('Player Health:', player_health)
    return player_health

# fight(player_health, equippedList, inventory):
#     Checks To see if Hi-c and Bicycle in inventory to update distance
#     Uses Boolean flag for input validation
#     Calls Function fightOptions()
#          if input == Fight
#             Calls Function fight()
#             The Fight Begins
#          if input ==  Flail
#             player_health = 0
#          if input == flee
#             70% chance
#                 player_health is subtructed by base attack or demogragon
#                 divided by two
#             30% chance
#                 player_health is restored to max_health
# Input: player_health, equippedList, inventory; current status of parameters.
# Output: healthdist; list( player_health, distTravelled, demoHealth )
def fight(player_health, equippedList, inventory, distTravelled):
    inventory = inventory
    equipped = "".join(equippedList)
    player_health = player_health
    demoHealth = DEMOG_MAX_HEALTH
    demoPower = DEMOG_BASE_ATTACK
    distTravelled = distTravelled
    halfed = 0.5
    quartered = 0.25
    print("The Demogorgon appears in front of you. You must do something!\n")
    #Checks if certian items are in your inventory to apply their power.
    if 'Hi-C' in inventory:
        demoHealth = DEMOG_MAX_HEALTH * halfed
        print('Heath of Demogorgon is: ', demoHealth)
    if 'Walkman' in inventory:
        demoPower = DEMOG_BASE_ATTACK - (DEMOG_BASE_ATTACK * quartered)
        print('Power of Demogorgon is: ', demoPower)
    flag = False
    while not flag and player_health > MIN_HEALTH and demoHealth > MIN_HEALTH:
        flag = True
        #Calls functions to get user input
        optChosen = fightOptions()
        actionChosen = optChosen

        # Calculates player health by damaged applied
        if actionChosen == 1:
            damage = calcDamage(equipped)
            if equipped in inventory:
                demoHealth -= damage
                print("\nYou've attacked with " + equipped + " causing a "
                      "damage of " + str(damage) + "\nDemogorgon heath "
                      "is :",demoHealth)
            player_health -= demoPower
            print('\nDemogorgon has atackked you with base attack ' +
                  str(demoPower) + " \nPlayer health is:",
                  player_health)
            print('')
            distTravelled = travelledDist(player_health)
            flag = False
        if player_health <= MIN_HEALTH:
            print('Dead')

        # Uses while loop calculate player health to become 0. Fun way to do it!
        if actionChosen == 2:
            while player_health > 0:
                player_health -= demoPower
            print('\nThe Demogorgon has knocked you out!')
            distTravelled = travelledDist(player_health)

        # Flee
        if actionChosen == 3:
            fleeChance = randint(1, 10)
            # Player health is restored to 100
            if fleeChance <= 3:
                player_health = player_health
                distTravelled = travelledDist(player_health)
                print("\nYou have escaped")
                print("Player health: ", player_health)
            # Player health is subtructed by 10
            elif 4 <= fleeChance <= 10:
                player_health -= (DEMOG_BASE_ATTACK * halfed)
                print("\nThe Demogorgon has attacked you with base attack 10.")
                print("Player health: ", player_health)
                print('')
                distTravelled = travelledDist(player_health)
                flag = False
            if player_health <= MIN_HEALTH:
                print('Dead')
        # Evaluates Final Health of Player and Demogragon
        if player_health <= MIN_HEALTH:
            print("\nFinal Player health is:", MIN_HEALTH)
            print("Final Demogorgon health is:", demoHealth)
        if demoHealth <= MIN_HEALTH:
            print("\nFinal Demogorgon health is:", MIN_HEALTH)
            print("Final Player health is:", player_health)

        healthdist = []
        healthdist.append(player_health)
        healthdist.append(distTravelled)
        healthdist.append(demoHealth)
    return healthdist

# def randomWalkingEvents(randomNum, randomFood, randomItem, equippedList,
#                         inventory, player_health, distTravelled):
#     CALLS FUNCTION travelledDist
#     distTravelled = travelledDist(player_health)
#     1 - 20% CHANCE
#       Event 3: Find Food
#       Calls Function eat(food, player_health)
#     2 - 20% CHANCE
#         Event 3: Find an item
#         itemFound = ITEMS_IN_SHED[randomItem]
#         appends itemFound to inventory
#     3 - 20% CHANCE
#         Event 3: Fall into a Trench
#           Distance is halfed
#           another day passes
#     4 - 30% CHANCE
#       Event 3: Demogragon appears
#       Calls Function fight(player_health, equippedList, inventory)
#     1 - 10% CHANCE
#         Nothing happens
# Input: randomNum, randomFood, randomItem, equippedList, inventory,
#        player_health, distTravelled; current status of parameters.
# Output: healthDistList; list(player_health, distTravelled, distSum, day)
#         current status of variables.
def randomWalkingEvents(randomNum, randomFood, randomItem, equippedList,
                        inventory, player_health, distTravelled,
                        distTravelledList, distSum, day):

    distTravelled = travelledDist(player_health)
    inventory = inventory
    equipped = "".join(equippedList)
    player_health = player_health

    # 20% chance you find a random food
    if 1 <= randomNum <= 2:
        food = BACKPACK_ITEMS[randomFood]
        print("\nAs you were walking you found a backpack. \nInside the "
              "backpack, there is food:", food)
        toEat = eatOptions()
        if toEat == 1:
            print("You've chosen to eat", food)
            player_health = eat(food, player_health)
            distTravelled = travelledDist(player_health)
        if toEat == 2:
            print("You've chosen not to eat", food)

    # 20% chance you find a random item
    if 3 <= randomNum <= 4:
        itemFound = ITEMS_IN_SHED[randomItem]
        print('\nYou pass by and old shed and decide to go inside. Something '
              'on the shelf catches your eye. \nYou reach up to grab the item. '
              'Its a', itemFound)
        inventory.append(itemFound)
        print(itemFound, "has been added to your invetory")
        print(inventory)

    # 20% chance you fall into a trench
    if 5 <= randomNum <= 6:
        print("\nYou fell into a trench becuase you weren't paying attention "
              "to where you were stepping. \nIt takes you a whole extra day "
              "to climb out \nYou've travelled only half the distance")
        distTravelled = distTravelled / 2
        day += 1
        player_health = player_health

    # 30% chance you come face to face with the Demogragon
    # fight() function is called
    if 7 <= randomNum <= 9:
        print("\nThe Demogorgon catches up to you. ")
        healthDistList = fight(player_health, equippedList, inventory,
                               distTravelled)
        player_health = healthDistList[0]
        distTravelled = travelledDist(player_health)
        demoHealth = healthDistList[2]
        if demoHealth <= MIN_HEALTH:
            demoHealth = MAX_HEALTH

    # 10% chance you nothing happens
    if randomNum == 10:
        print('\nNothing happens.')
        player_health = player_health
        distTravelled = travelledDist(player_health)

    # Checks to see if certain items are in inventory to apply item power.
    if 'Bicycle' in inventory:
        distTravelled = distTravelled * BICYCLE_POWER
        print("The Bicycle you found improved your distance traveled.")
    elif 'Heelys' in inventory:
        distTravelled = distTravelled * HEELYS_POWER
        print("The Heelys you found improved your distance traveled.")

    distTravelledList.append(distTravelled)
    print("\nYou've travelled distance: ",distTravelled, 'miles')
    healthDistList = []
    healthDistList.append(player_health)
    healthDistList.append(distTravelled)
    healthDistList.append(distSum)
    healthDistList.append(day)
    return healthDistList

# stayPut(randomNum, equippedList, player_health, inventory):
#     30% chance
#         Player health restores to MAX HEALTH
#     70% Chance
#         DEOMGRAGON CATCHES UP TO YOU
#         CALLS FUNCTION fight(player_health, equippedList, inventory)
# Input: randomNum, equippedList, player_health; current status of parameters.
# Output: healthDistList; list(player_health, distTravelled); current value
#         of variables
def stayPut(randomNum, equippedList, player_health, inventory):
    inventory = inventory
    equipped = "".join(equippedList)
    player_health = player_health
    distTravelled = travelledDist(player_health)

    # 30% Chance you evade the demogragon
    if randomNum <= 3:
        print('You have successfully evaded the monster')
        player_health = MAX_HEALTH
        print("Player health has been restored to:", MAX_HEALTH)
        player_health = player_health

    # 70% Chance the demogragon finds you
    # fight() function is called
    if 4 <= randomNum <= 10:
        print('\nThe Demogorgon reaches your camp!')
        healthDistList = fight(player_health, equippedList, inventory,
                           distTravelled)
        player_health = healthDistList[0]
        demoHealth = healthDistList[2]
        if demoHealth <= MIN_HEALTH:
            demoHealth = MAX_HEALTH

    healthDistList = []
    healthDistList.append(player_health)
    healthDistList.append(distTravelled)
    return healthDistList

# stayOrGo(item, inventory, player_health, distTravelled):
#     USING BOOLEAN FLAG
#         RANDOMISES NUMBERS - RANDIT FUNCTION IS CALLED
#         INPUT VALIDATION - for leaveOrStay
#         if leaveOrStay == 1
#             CALLS FUNCTION randomWalkingEvents(randomNum, randomFood,
#                            randomItem, equippedList, inventory,
#                            player_health, distTravelled)
#         elif leaveOrStay == 2:
#             CALLS FUNCTION stayPut(randomNum, equippedList, player_health)
# Input: item, inventory, player_health, distTravelled; current status of
#        parameters.
# Output: healthDistList; list(player_health, distTravelled, distSum, day);
#         current value of variables
def stayOrGo(item, inventory, player_health, distTravelled,
             distTravelledList, distSum, day, flag):
    inventory = inventory
    while not flag:
        randomNum = randint(1, 10)
        randomFood = randint(0, len(BACKPACK_ITEMS) - 1)
        randomItem = randint(0, len(ITEMS_IN_SHED) - 1)
        flag = True
        print("\nThe Demogorgon looms in the distance")
        print("Your options are:\n1 - Pack up camp and go \n2 - Stay where "
              "you are")
        leaveOrStay = int(input('Enter a choice: '))
        # Input Validation
        if leaveOrStay != 1 and leaveOrStay != 2:
            print('\nPlease enter a valid choice')
            flag = False

        # randomWalkingEvents() function is called
        if leaveOrStay == 1:
            print('\nYou have began heading in the direction of the nearest '
                  'town.')
            equippedList = item
            healthDistList = randomWalkingEvents(randomNum, randomFood,
                           randomItem, equippedList, inventory,
                           player_health, distTravelled, distTravelledList,
                                                 distSum, day)
            player_health = int(healthDistList[0])
            distTravelled = float(healthDistList[1])
            distSum = healthDistList[2]
            day = healthDistList[3]

        # stayPut() function is called
        elif leaveOrStay == 2:
            print("\nYou have chosen to stay put")
            equippedList = item
            healthDistList = stayPut(randomNum, equippedList, player_health,
                                    inventory)
            player_health = int(healthDistList[0])
            distTravelled = float(healthDistList[1])

    healthDistList = []
    healthDistList.append(player_health)
    healthDistList.append(distTravelled)
    healthDistList.append(distSum)
    healthDistList.append(day)
    return healthDistList

# main():
#
#     while player_health > 0 and day < DAYS_TO_SURVIVE and distTravelled < \
#             MILES_TO_SURVIVE:
#         RANDOM FUNCTIONS FROM IMPORT RANDIT
#         CALLS THE BIG&MAIN FUNCTIONS
#         calculateDailyTask(equippedItem, player_health, inventory,
#         distTravelled)
#         stayOrGo(item, inventory, player_health, distTravelled)
#         day += 1 UPDATES DATE
#       CHECKS TO SEE IG GAME IS WON OR LOST
#          distTravelled > MILES_TO_SURVIVE or day >= DAYS_TO_SURVIVE:
#             You've won!
#          player_health < 0 or day < DAYS_TO_SURVIVE or distTravelled < \
#             MILES_TO_SURVIVE:
#             You have Lost!
def main():
    day = int(0)
    distSum = float(0)
    player_health = int(100)
    distTravelled = float(0)
    distTravelledList = []
    index = 0
    inventory = ['Walkie Talkie', 'Flashlight']
    equippedItem = []
    eaten = False
    flag = False

    # Game Instructions
    print('\nLet the Games Begin. This is a text-based adventure game. \nThe '
          'premise of this game is that you went camping in the woods only' 
          ' to find out that a monster, \nThe Demogorgon, was set loose from '
          'the lab conveniently located in the same forest. \nThe object of '
          'this game is to run away from that monster. If you can stay alive '
          'for seven days, \nor if you travel 150 miles to the nearest big '
          'city, then you win the game. \nIf you die at the hands of the '
          'monster, or by some other means, you lose the game!')


    while player_health > 0 and distSum < MILES_TO_SURVIVE and day < \
            DAYS_TO_SURVIVE:
        print('\nDay', day + 1, '\n')

        # Calls function calculateDailyTask()
        equipHealth = calculateDailyTask(equippedItem, player_health,
                                         inventory, distSum, eaten)

        item = equipHealth[0]
        player_health = equipHealth[1]

        # Calls function stayOrGo()
        healthDistList = stayOrGo(item, inventory, player_health,
                                distTravelled, distTravelledList, distSum,
                                  day, flag)
        # Updates variables
        player_health = int(healthDistList[0])
        distTravelled = float(healthDistList[1])
        day = healthDistList[3]
        distSum = int(healthDistList[2])
        day += 1
        eaten = False

        #Calculates Total Distance
        while index < len(distTravelledList):
            distSum += distTravelledList[index]
            print("Total Distance:",distTravelledList,'=', distSum, 'miles')
            index += 1

    # Evaluates variables to check if the player has met the games
    # requirement to win or loose the game
    if distSum > MILES_TO_SURVIVE or day >= DAYS_TO_SURVIVE:
        if player_health <= 0 and day >= DAYS_TO_SURVIVE or distSum >= \
                MILES_TO_SURVIVE:
            print('\nGame Over - You have Lost!')
        elif player_health > 0 and day >= DAYS_TO_SURVIVE:
            print("\nYOU'VE WON!!!!")
    elif player_health < 0 or day < DAYS_TO_SURVIVE or distSum < \
            MILES_TO_SURVIVE:
        print('\nGame Over - You have Lost!')


main()
