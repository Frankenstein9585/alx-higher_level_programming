#!/usr/bin/python3
def print_last_digit(number):
    last = 0
    if number == 0:
        last = 0
    elif number < 0:
        last = (number % 10 - 10) * -1
    else:
        last = number % 10
    print('{:d}'.format(last), end ='')

print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)
