import random

attempts = 0

while True:
    try:
        x = int(input("Enter number: "))
    except ValueError:
        print("Please enter an integer")
    else:
        comp = random.randint(0, 10)
        if x != comp:
            attempts += 1
            print('Try again')
        else:
            print(f'You guessed right! it took you {attempts} attempts')
            break
































