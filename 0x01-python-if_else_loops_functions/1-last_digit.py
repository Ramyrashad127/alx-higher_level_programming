#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10

if number < 0:
    digit = -1 * digit
if digit > 5:
    print("Last digit of", number, "is", digit, "and is greater than 5")
elif ((digit != 0) and (digit < 6)):
    print("Last digit of", number, "is", digit, "and is less than 6 and not 0")
else:
    print("Last digit of", number, "is", digit, "and is 0")
