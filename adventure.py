import os
import time
from functions import *
os.system("cls")
#Collect character name to use in dialog later on
print("If you see a sentence encapsulated in \"*\" then input is required.")
#time.sleep(2.0)
input("Press enter when you are ready to begin your journey.")
os.system("cls")
raw_character_name = input("*What is your characters name?* \n")
delete_user_input()
#For the sake of readability, make sure the name isn't too long
while not raw_character_name.isalpha():
    print(raw_character_name + " contains illegal characters, please enter another name.")
    raw_character_name = input("What is your characters name? \n")
    delete_user_input()
else:
    character_name = raw_character_name.title()
while len(raw_character_name) > 15:
    print("Please make your character name less than 15 letters long.")
    raw_character_name = input("What is your characters name? \n")
else:
    character_name = raw_character_name.title()
os.system('cls')
#Setting the scene for the player to make their first decision
print("You wake up in the middle of a small forest, unaware of your surroundings.")
#time.sleep(2.0)
print("You know two things for certain, you feel very hungover and you must get out of there.")
#time.sleep(2.0)
print("As you try to gather yourself you realize that you can either decide to go back to sleep or to stand up and look around. \n")
#time.sleep(4.0)
#First choice for the player - 1.1/1.2 look around or sleep
option1 = input("*Look around* *Sleep* \n").lower()
delete_user_input()

#While statement prevent player from moving forward unless the correct input is given
while option1 != "look around" and option1 != "sleep":
    print("Please select one of the available options.")
    option1 = input("*Look around* *Sleep* \n").lower()
    delete_user_input()
else:
    #After correct input is given check which one it is and direct the story accordingly
    if option1 == "sleep":
        print("You chose to " + option1 + ".")
        #time.sleep(2.0)
        print("You wake up the next day feeling very groggy but no longer hungover.")
        #time.sleep(2.0)
        print("While laying down you come to 2 conclusions on what to do next.")
        #time.sleep(2.0)
        print("You decide that you could sleep some more and hope you feel 100% tomorrow.")
        #time.sleep(2.0)
        print("Or you can stand up and look around for a way out of the forest.\n")
        #time.sleep(2.0)
        option1_1 = True
    if option1 == "look around":
        print("You chose to " + option1 + ".")
        #time.sleep(2.0)
        print("Although you still feel sick you decide it is best to get up and look around.")
        #time.sleep(2.0)
        print("As you stand up your stomach quickly turns cause you to expel whatever contents were in your stomach from the night before.")
        #time.sleep(4.0)
        print("You gather yourself and notice there are 2 paths out of the forest.")
        #time.sleep(2.0)
        print("The first path is extremely ordinary with nothing of note sticking out.")
        #time.sleep(2.0)
        print("As you look over to the second path you notice a massive billowing smoke cloud above the tree line.\n")
        #time.sleep(3.0)
        option2 = True
        option1_1 = False
        option1_5 = False

if option1_1:
    option1_1 = input("*Look around* *Sleep* \n").lower()
    delete_user_input()
    while option1_1 != "look around" and option1_1 != "sleep":
        print("Please select one of the available options.")
        option1_1 = input("*Look around* *Sleep* \n").lower()
        delete_user_input()
    else:
        if option1_1 == "sleep":
            print("You chose to " + option1_1 + ".")
            #time.sleep(2.0)
            print("You wake up the next day feeling even better than the day before.")
            #time.sleep(2.0)
            print("No longer feeling groggy you decide on 2 options on how to move forward.")
            #time.sleep(2.0)
            print("Since you feel so good after that sleep, you contemplate sleeping again.")
            #time.sleep(2.0)
            print("Or you could get up and find a way out of the forest you've been sleeping in.\n")
            #time.sleep(2.0)
            option1_2 = True
        if option1_1 == "look around":
            print("You chose to " + option1_1 + ".")
            #time.sleep(2.0)
            print("You wake up the next day feeling even better than the day before.")
            #time.sleep(2.0)
            print("After gaining that extra night of sleep you feel ready make your way out of the forest.")
            #time.sleep(2.0)
            print("You notice there are 2 path you can take.")
            #time.sleep(2.0)
            print("The first path is very ordinary with nothing prominent catching your eye.")
            #time.sleep(2.0)
            print("As you look over to the second path you notice a big smoke cloud extending into the sky just above the tree line.\n")
            #time.sleep(4.0)
            option2 =True
            option1_2 = False

    if option1_2 == True:
        option1_2 = input("*Look around* *Sleep* \n").lower()
        delete_user_input()
        while option1_2 != "look around" and option1_2 != "sleep":
            print("Please select one of the available options.")
            option1_2 = input("*Look around* *Sleep* \n").lower()
            delete_user_input()
        else:
            if option1_2 == "sleep":
                print("You chose to " + option1_2 + ".")
                #time.sleep(2.0)
                print("Besides being hungry and slightly dehydrated you wake up feeling the best you have felt in a very long time.")
                #time.sleep(4.0)
                print("Feeling reinvigorated you feel like now might be the best time to get out of the forest.")
                #time.sleep(3.0)
                print("You can't stop thinking about how good that sleep was and start to consider sleeping just one more day.")
                #time.sleep(3.0)
                print("You take a quick seat and decide if you want to go back to sleep or look for a way out.\n")
                #time.sleep(2.0)
                option1_3 = True
            if option1_2 == "look around":
                print("You chose to " + option1_2 + ".")
                #time.sleep(2.0)
                print("You have now slept for 3 days and feel like a brand new man.")
                #time.sleep(2.0)
                print("Noticing there are 2 paths you can take you look over at the first one.")
                #time.sleep(2.0)
                print("This path is just an ordinary path, there is nothing prominent enticing you to go that way.")
                #time.sleep(3.0)
                print("You look over to the other path and notice there is a small billow of smoke over the tree line.\n")
                #time.sleep(3.0)
                option2 = True
                option1_3 = False

    if option1_3:
        option1_3 = input("*Look around* *Sleep* \n").lower()
        delete_user_input()
        while option1_3 != "look around" and option1_3 != "sleep":
            print("Please select one of the available options.")
            option1_3 = input("*Look around* *Sleep* \n").lower()
            delete_user_input()
        else:
            if option1_3 == "sleep":
                print("You chose to " + option1_3 + ".")
                #time.sleep(2.0)
                print("My guy, you've slept long enough, you could really use some food and water.")
                #time.sleep(2.0)
                print("It's well past time to look around.")
                #time.sleep(2.0)
                print("What's the plan?\n")
                #time.sleep(1.0)
                option1_4 = True
            if option1_3 == "look around" or option1_3 == "look around":
                print("You chose to " + option1_3 + ".")
                #time.sleep(2.0)
                print("You are very hungry and thirsty, so you finally decide to look for a way out of the forest.")
                #time.sleep(3.0)
                print("Looking left and right you quickly notice there are 2 paths you can take.")
                #time.sleep(2.0)
                print("One path is basic as can be, there is nothing standing out that interests you.")
                #time.sleep(2.0)
                print("As you look over to the second path you notice a very small column of smoke rising above the tree line.")
                #time.sleep(2.0)
                option2 = True
                option1_4 = False

    if option1_4:
        option1_4 = input("*Look around* *Sleep* \n").lower()
        delete_user_input()
        while option1_4 != "look around" and option1_4 != "sleep":
            print("Please choose one of the provided options.")
            option1_4 = input("*Look around* *Sleep* \n").lower()
            delete_user_input()
        else:
            print("You chose to " + option1_4 + ".")
            #time.sleep(2.0)
            print("You're kidding right.....")
            #time.sleep(2.0)
            print("Since all you wanna do is sleep, it looks like I'll have to play the game for you.")
            #time.sleep(3.0)
            print("You \"choose\" to look around :) \n")
            option1_5 = True
            #time.sleep(2.0)

    if option1_5:
        print("Congratulations we can continue!")
        #time.sleep(2.0)
        print("You reluctantly rise to your feet to your feet, and process your surroundings.")
        #time.sleep(2.0)
        print("To your right is the most basic of basic paths that there ever has been, and ever will be.")
        #time.sleep(3.0)
        print("To your left you should have seen a big smoke cloud reaching into the sky just over the tree line.")
        #time.sleep(3.0)
        print("BUT, since you slept for so long there is no smoke cloud. \n")
        #time.sleep(2.0)
        option2 = True

if option2:
    option2 = input("*Ordinary* *Smoke Cloud* \n").lower()
    delete_user_input()
    while option2 != "ordinary" and option2 != "smoke cloud":
        print("Please choose one of the available options.")
        option2 = input("*Ordinary* *Smoke Cloud* \n").lower()
        delete_user_input()
    else:
        #Start of option 2 ORDINARY 
        if option2 == "ordinary":
            print("You chose the " + option2 + " path.")
            #time.sleep(2.0)
            print("You make your way down the ordinary path, taking in the scenery.")
            #time.sleep(2.0)
            print("While walking you are suspicious of how ordinary the path seems, so you examine your surrounding, hoping to find something interesting.")
            #time.sleep(4.0)
            print("Passing a deer munching some leaves, 2 squirrels fighting over a nut, you come to realize it is just an ordinary path.")
            #time.sleep(3.0)
            print("After a couple of minutes you eventually see a break in the trees that opens into an expansive field.")
            #time.sleep(3.0)
            print("You see a town off in the distance, what appears to be an hour walk.")
            #time.sleep(2.0)
            print("Thinking that the walk is pretty long you think about seeing if there is anything in the field.")
            #time.sleep(3.0)
            option3 = True
        #Start of the option 2 SMOKE CLOUD 
        if option2 == "smoke cloud" and option1_5 == True:
            less_food = True
            print("You chose the " + option2 + " path.")
            #time.sleep(2.0)
            print("Although you are upset that you slept through the massive smoke cloud, you still decide to go in that direction.")
            #time.sleep(3.0)
            print("As you get closer to the edge of the forest you can hear some grumbling, unsure of what it is.")
            #time.sleep(2.0)
            print("The tree density is starting to dwindle and you realize you are about to walk out of the forest.")
            #time.sleep(3.0)
            print("You break through the forest, tripping on branch. You gather yourself and look upon a massive fair taking place.")
            #time.sleep(3.0)
            print("You realize the grumbling was actually cheers and chatter from town folk. As your stomach yearns for food you scan the fair to see what to do.")
            #time.sleep(5.0)
            #Add option to pick food, games, entertainment. Look into being able to switch one to the other without just reusing blocks of code, but I feel like that wont be possible
            #NESTING: having variables too far in nested statements might and will probably cause problems 
        elif option2 == "smoke cloud":
            print("You chose the " + option2 + " path.")
            #time.sleep(2.0)
            print("Intrigued by the smoke cloud you saw, not knowing if you should fear the worst, you take off down the path.")
            #time.sleep(3.0)
            print("Rushing through the forest you try to prepare yourself for whatever might be ahead.")
            #time.sleep(3.0)
            print("As the forest becomes more scare you come upon the edge so you burst through and instantly start looking for the cause of the fire.")
            #time.sleep(4.0)
            print("You quickly realize that the fire is just a massive bonfire in the center of a town fair.")
            #time.sleep(3.0)
            print("Relieved that nothing tragic or nefarious has happened, you look around to see what the fair has to offer.")
            #time.sleep(2.0)
            #Add option for player to pick food, games, entertainment with the same potential logic as above