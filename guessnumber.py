import random
number=random.randint(1,9)
chances=0
while chances<5:
    guess=int(input("guess a number between 1 and 9 : "))
    if guess==number:
        print("you won lol")
        break
    else:
        chances=chances+1
        if guess>number:
            print("your guess was too high")
        else:
            print("your guess was too low")

        print("You have", 5-chances, "chances left.")
if chances == 5:
    print("Sorry, you used all your chances. The number was", number)

    
 