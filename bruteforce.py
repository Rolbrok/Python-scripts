#!/usr/bin/python

import sys

length = 6
if len(sys.argv) == 2: length = int(sys.argv[1])

alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
max_length = len(alphabet)-1

chars = [alphabet[0] for i in range(length)]

currPos = 0

def getPos(char):
    global alphabet
    for x, i in enumerate(alphabet):
        if i == char: return x

for i in range(length**max_length):
    try:
        print("".join(chars))
        if currPos <= max_length:
            chars[-1] = alphabet[currPos]
            currPos += 1
        else:
            currPos = 0

        for z in range(len(chars)-1,0,-1):
            pos = getPos(chars[z])
            #print(z, pos)
            if pos >= max_length:
                chars[z-1] = alphabet[getPos(chars[z-1]) + 1]
                chars[z] = alphabet[0]
        if getPos(chars[0]) >= max_length: chars[0] = alphabet[0]
    except:
        print("Quitting...")
        exit(0)
