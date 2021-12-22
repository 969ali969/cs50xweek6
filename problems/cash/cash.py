from cs50 import get_float

# Get input from user and make sure its correct
while True:
    user_number = get_float("Change owed: ")
    if user_number >= 0.001:
        break


# Multiply by 100
DtC = round(user_number * 100)


# Calculator 25
counter25 = 0
cent25 = DtC
while cent25 >= 25:
    counter25 += 1
    cent25 -= 25

# Calculator 10
counter10 = 0
cent10 = cent25
while cent10 >= 10:
    counter10 += 1
    cent10 -= 10

# Calculator 5
counter5 = 0
cent5 = cent10
while cent5 >= 5:
    counter5 += 1
    cent5 -= 5

# Calculator 1
counter1 = 0
cent1 = cent5
while cent1 >= 1:
    counter1 += 1
    cent1 -= 1


# All coin used
last = counter25 + counter10 + counter5 + counter1
print(last)
