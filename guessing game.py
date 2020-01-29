import random
import winsound
print("I'm thinking of a number between 0 and 100.")
num = random.randint(0, 100)
guess = None
while guess != num:
    try:
        guess = int(input("Your guess: "))
    except ValueError:
        print("That's not a number. Restarting program...")
        continue
    try:
        if guess > 100:
            print("That's higher than 100!")
        elif guess < 0:
            print("That's lower than 0!")
        elif guess > num:
            print("Lower!")
        elif guess < num:
            print("Higher!")
        else:
            print("I can't compute that. Try again!")
print('''You got it!___       ___            ___        ___   __
            \  \      /  /     /\      \  \      /  /   |  |
             \  \   /  /     /   \      \  \   /  /     |  |
              \  \/  /     /      \      \  \/  /       |  |
               \    /     /   /\   \      \    /        |  |
                \  /    /   /__\   \      \  /         |  |
                |  |   /  ______   \     |  |         |__|
                |  | /  /          \   \    |  |         __
                |  |/  /             \  \   |  |         |  |
                |_|_/                \_\   |_|         |_|
             ''')
        winsound.Beep(262, 100)#c
        winsound.Beep(294, 100)#d
        winsound.Beep(330, 100)#e
        winsound.Beep(349, 100)#f
        winsound.Beep(392, 100)#g
        winsound.Beep(440, 100)#a
        winsound.Beep(494, 100)#b
        winsound.Beep(600, 1000)#b
    except ValueError:
        print("That's not a number. Restarting program...")
        break
