#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number == 0:
    print('Last digit of 0 is 0')
    exit()
last_digit = number % 10 - 10 if number < 10 else number % 10
print(f'Last digit of {number} is {last_digit}', end=' ')
if last_digit > 5:
    print('and is greater than 5')
elif last_digit == 0:
    print('and is 0')
else:
    print('and is less than 6 and not 0')
