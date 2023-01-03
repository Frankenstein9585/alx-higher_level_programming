#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) in range(ord('a'), ord('z') + 1):
            i = chr(ord(i) - 32)
        print("{:s}".format(i), end="")
    print()
