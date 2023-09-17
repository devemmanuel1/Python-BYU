print('Welcome to the text-based adventure game! \n The Title of the game is ')

first_left = '\nAfter entering the left tunnel, you continue going until you spot a faint light in the distance. Do you want to go toward the light or disregard it and keep going?\n'

first_right = '\n After going for a time after entering the right tunnel, you come to a junction in the road. The right way appears large and straightforward whereas the left path appears slender and steep. Which direction do you wish to go? RIGHT or LEFT? \n'

second_left = '\n After taking a few steps down the left route, a loud growling sound can be heard. When you turn around, a huge dragon is in your path. Do you prefer to fight or run away? \n'

second_right = '\n You take the right route, and after a few steps, you come across a beautiful underground lake. You can see something shining in the water. Do you want to DIVE in and retrieve it or continue WALKING around the lake? \n'

approach = '\n You approach the light and find a treasure chest. The chest is locked with a combination. You can see some numbers scratched on the wall next to it. Do you want to try the combination? YES or NO? \n'

ignore = '\n You continue walking, but suddenly the ground beneath you gives way, and you fall into a pit trap. You try to climb out, but the walls are too steep. You are trapped. Game over. \n'

yes = '\n You try the combination and the chest unlocks. Inside, you find a map that shows the way out of the cave. You can also see a glint of something shiny in the corner. Do you want to take the MAP or the SHINY OBJECT? \n'

no = '\nYou decide not to try the combination and continue following your instincts. After a few twists and turns, you find yourself back outside the cave. Congratulations, you have made it out alive!\n'

map1 = '\nYou decide to take the map. After a few twists and turns, you find yourself back outside the cave. Congratulations, you have made it out alive!\n'

shiny_object = '\n You pick up the shiny object, and suddenly you hear a loud noise. You turn around and see a group of goblins rushing towards you. Do you want to FIGHT or RUN? \n'

run = '\n You run as fast as you can, and the goblins chase you for a while, but they eventually give up. You continue following the map, and after a few twists and turns, you find yourself back outside the cave. Congratulations, you have made it out alive! \n'

fight1 = '\n You fight bravely, but there are too many goblins. They overpower you, and you fall to the ground. The last thing you see before you lose consciousness is the shiny object rolling away from you. Game over. \n'

fight2 = '\n You draw your sword and charge at the dragon. The dragon breathes fire, but you manage to dodge it and strike the dragon with your sword. The dragon roars in pain and takes flight. You continue down the path and eventually come across a hidden stash of gold coins. Congratulations, you have found a treasure! \n'

flee = '\n You turn around and run as fast as you can. The dragon chases you for a while, but eventually gives up. You continue down the path and eventually come across a hidden stash of gold coins. Congratulations, you have found a treasure! \n'

dive = '\n You take a deep breath and dive into the lake. You swim towards the shiny object and find a pearl necklace. As you are swimming back to the surface, you feel something brush against your leg. Do you want to continue swimming to the SURFACE or PANIC and swim back down? \n'

walk = '\n You continue walking around the lake, and eventually, you see a hidden cave entrance. You enter the cave and find a secret chamber filled with treasure. Congratulations, you have found a valuable treasure! \n'

surface = '\n You swim to the surface and take a deep breath. As you look around, you see that the lake is filled with harmless fish. You continue walking and eventually find a way out of the cave. Congratulations, you have made it out alive with a valuable treasure! \n'

panic = '\n You start swimming back down, but your panic causes you to lose your way. You get tangled in some seaweed and cannot free yourself. You drown in the lake. Game over.\n'

side = '\n After taking the side path, the user encounters a deep chasm. There is a narrow bridge across the chasm, but it looks old and rickety. The user can either CROSS the bridge or TURN BACK. \n'

cross ='\n You carefully make your way across the narrow bridge. It creaks and sways under your weight, but you manage to reach the other side. As you continue along the path, you find a small chest hidden behind some rocks. Do you want to OPEN the chest or LEAVE it? \n'

turn = '\n You turned back, now you have to take either of the tunnels in the cave\n'

open = '\n Congratulations You open the chest and find a potion that restores your health. You feel invigorated and ready to continue your adventure. You follow the path and eventually emerge from the cave, victorious. \n'

leave = '\n You decide to leave the chest behind and continue on your way. As you walk, you suddenly feel a sharp pain in your side. You look down and see a dart sticking out of your skin. You realize too late that the chest was booby-trapped. Game over.'

invalid_input = '\n Invalid input. Please try again. \n'

print("You are now in front of the strange cave's entrance. A trail at the side of the cave and two tunnels going in opposing directions are visible. Which would you like to choose? the RIGHT or LEFT SIDE?\n ")

left_right_or_side = input("Please enter your choice LEFT, RIGHT or SIDE? ").lower()


if left_right_or_side == 'left':
    print(first_left)
    approach_or_ignore = input('Please enter your choice: APPROACH or IGNORE? ').lower()
    if approach_or_ignore == 'approach':
        print(approach)
        yes_or_no = input('Please enter your choice: YES or NO? ').lower()
        if yes_or_no == 'yes':
            print(yes)
            map_or_shiny = input('Please enter your choice: MAP or SHINY OBJECT? ').lower()
            if map_or_shiny == 'shiny object':
                print(shiny_object)
                fight_or_run = input('Please enter your choice: FIGHT or RUN? ').lower()
                if fight_or_run == 'run':
                    print(run)
                elif fight_or_run == 'fight':
                    print(fight1)
                else:
                    print(invalid_input)
            elif map_or_shiny == 'map':
                print(map1)
        elif yes_or_no == 'no':
            print(no)
        else:
            print(invalid_input)
    elif approach_or_ignore == 'ignore':
        print(ignore)
    else:
        print(invalid_input)
elif left_right_or_side == 'right':
    print(first_right)
    second_left_right = input('Please enter your choice: LEFT or RIGHT? ').lower()
    if second_left_right == 'left':
        print(second_left)
        fight_or_flee = input('Please enter your choice: FIGHT or FLEE? ').lower()
        if fight_or_flee == 'fight':
            print(fight2)
        elif fight_or_flee == 'flee':
            print(flee)
        else:
            print(invalid_input)
    elif second_left_right == 'right':
        print(second_right)
        dive_or_walk = input('Please enter your choice: DIVE or WALK? ').lower()
        if dive_or_walk == 'dive':
            print(dive)
            surface_or_panic = input('Please enter your choice: SURFACE or PANIC? ').lower()
            if surface_or_panic == 'surface':
                print(surface)
            elif surface_or_panic == 'panic':
                print(panic)
            else:
                print(invalid_input)
        elif dive_or_walk == 'walk':
            print(walk)
        else:
            print(invalid_input)
    else:
        print(invalid_input)

elif left_right_or_side == 'side':
    print(side)
    cross_or_turn = input('Please enter your choice: CROSS or TURN? ').lower()
    if cross_or_turn == 'cross':
        print(cross)
        open_or_leave = input('Please enter your choice: OPEN or LEAVE? ')
        if open_or_leave == 'open':
            print(open)
        elif open_or_leave == 'leave':
            print(leave)
        else:
            print(invalid_input)
    elif cross_or_turn == 'turn':
        print(turn)
    else:
        print(invalid_input)
else:
    print(invalid_input)
    






