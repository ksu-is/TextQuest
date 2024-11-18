def start_game():
    print("Welcome to TextQuest! You will be faced will multiple choices. These choices will decide your fate.")
    print("While you are walking a trail, you find yourself in front of a dark forest. What will you do?")
    
    while True:
        print("\n1. Enter the forest")
        print("2. Stay on the path")
        print("3. Turn back.")
        choice = input("What do you want to do? (1, 2, or 3): ").strip()

        if choice == "1":
            enter_forest()
        elif choice == "2":
            stay_on_path()
        elif choice == "3":
            print("You decide to turn around and leave. Game over.")
            break
        else:
            print("Invalid choice, please try again.")

def enter_forest():
    print("\nYou enter the dark forest.")
    print("You hear strange sounds all around you. What will you do next?")
    
    while True:
        print("\n1. Investigate the noises")
        print("2. Keep walking deeper into the forest")
        print("3. Climb a tree for a better view")
        choice = input("What do you want to do? (1, 2, or 3): ").strip()

        if choice == "1":
            investigate_noise()
            break
        elif choice == "2":
            deep_in_forest()
            break
        elif choice == "3":
            climb_tree()
            break
        else:
            print("Invalid choice, please try again.")

def stay_on_path():
    print("\nYou decide to stay on the path. The path is quiet, but you feel uneasy.")
    print("You see a small cabin up ahead. What will you do?")
    
    while True:
        print("\n1. Approach the cabin")
        print("2. Keep walking along the path")
        print("3. Turn back")
        choice = input("What do you want to do? (1, 2, or 3): ").strip()

        if choice == "1":
            approach_cabin()
            break
        elif choice == "2":
            print("You continue walking, but the path seems to go on forever. You decide to turn back.")
        elif choice == "3":
            print("You decide to turn back. Game over.")
            break
        else:
            print("Invalid choice, please try again.")

def investigate_noise():
    print("\nYou move toward the rustling noise. Suddenly, a raccooon jumps out of the bushes.")
    print("You laugh out of nervousness, but decide it's time to keep going.")
    
    next_step()

def deep_in_forest():
    print("\nYou walk further into the forest. The air grows cold.")
    print("Eventually, you come across a strange statue with unfamiliar wording.")
    print("What will you do?")
    
    while True:
        print("\n1. Examine the statue")
        print("2. Touch the statue")
        print("3. Turn back")
        choice = input("What do you want to do? (1, 2, or 3): ").strip()

        if choice == "1":
            examine_statue()
            break
        elif choice == "2":
            touch_statue()
            break
        elif choice == "3":
            print("You decide to turn back. You have an even more strange feeling walking around.")
            break
        else:
            print("Invalid choice, please try again.")

def climb_tree():
    print("\nYou climb a nearby tree to get a better view of your surroundings.")
    print("From up here, you can see a village far from the forest.")
    print("You climb down the tree, ready to go find the village.")
    
    next_step()

