import random
number=random.randint(1,10)

while True:
    guess=int(input("guess: "))
    if guess > number:
        print("decrease")
    elif guess == number:
        print("correct number")
        break
    else:
        print("increase")
       

