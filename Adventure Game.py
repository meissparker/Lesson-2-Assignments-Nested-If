# Task 1 # 2 and # 3

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass

elif place == "cave":     
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch":
        print("You see a monster!")
    elif action == "proceed in the dark": 
        print("You bump into something slimy.")
    else:
        pass

else:
    pass





