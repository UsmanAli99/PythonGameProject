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