import random

nums = int(input("Enter a number between 1 and 100: "))
number = random.randint(1,100)


if nums>number:
    print("Your number is too high!")
elif nums<number:
    print("You number is too low!")
else:
    print("You got it right!")


