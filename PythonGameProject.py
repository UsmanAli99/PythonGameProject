# Game Project
import sys
print("Welcome to the Game....")
name = input("Enter your name: ")
count = 0
while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        count += 1
        if count < 3:
            print("Error:/  Please, Enter valid age.....")
        else:
            sys.exit(1)
health = 10

if age >= 18:
    print(f"{name} are old enough to play!")
    want_to_play = input(f"{name} Do you want to play (yes / no): ").lower()
    if want_to_play == "yes":
        print(f"You are starting with {health} health!")
        print("Ok, Let's Play!")
        left_right = input("Choose where you want to go left or right (left / right): ").lower()
        if left_right == "left":
            print("Excellent! You follow the path and reach a lake!")
            ans = input("Do you want to swim across or go around (across / around): ").lower()
            if ans == "across":
                print("Excellent You went around and reached the other side of the lake!")
            else:
                print("You managed to get across, but were bit by the fish and lost 5 health!")
                health -= 5
            ans = input("You notice a river and house,choose  where do you want to go (house / river): ")
            if ans == "house":
                print("you go to the house and greeting with a person and he does not like you so you lost 5 health...")
                health -= 5
                if health <= 0:
                    print("You have 0 health so you lost the game....")
                else:
                    print("You Win!!!!!!")
            else:
                print("you fell down in the river and lost...")
        else:
            print("You fell down and lost!!!")
    else:
        print("Ok, By!!!!")
else:
    print("You are not old enough to play")