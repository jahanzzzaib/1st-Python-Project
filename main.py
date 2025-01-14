print('''
 _._     _,-'""`-._
(,-.`._,'(       |\`-/|
    `-.-' \ )-`( , o o)
          `-    \`_`"'-
''')
print("Welcome to the Treasure Island!")
print("Your mission is to find the treasure")

first_turn = input("You're at a cross-road. Where do you want to go?\n""     Type Left or Right\n")

if first_turn == "Left" or first_turn == "left":
    print("You've come to a Lake. There is an island in the middle of the lake.")
    boat_or_swim = input("Type 'Wait' to wait for a boat. Type 'Swim' to swim across.\n")
    if boat_or_swim == "Wait" or boat_or_swim == "wait":
        print("You arrive at the island unharmed. There is a house with three doors.")
        doors = input("One red, one yellow and one blue. Which one do you choose?\n")
        if doors == "red" or doors == "Red":
            print("TNT behind this door, goodbye. Game over")
        elif doors == "Yellow" or doors == "yellow":
            print("Congrats! You found the Treasure! (1000 vbucks) ")
        elif doors == "Blue" or doors == "blue":
            print("Long days you've opened the door to 5 hungry grizzly bears. Game over")
    if boat_or_swim == "Swim" or boat_or_swim == "swim":
        print("You just got eaten by a big fat shark. Game over")
elif first_turn == "Right" or first_turn == "right":
    print("You find a strange man offering a ride.")
    ride = input("Do you take the ride? Type 'Yes' or 'No' \n")
    if ride == "yes" or ride == "Yes":
        print("Yeah GGs you just got kidnapped and molested. Game over")
    elif ride == "no" or ride == "No":
        print("After you rejected him, the man got angry and ran you over. Game over")
else:
    print("Choose a direction brother")
