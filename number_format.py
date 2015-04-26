#!/usr/bin/python
import sys

def getposition(string, char):
    for pos, c in enumerate(string):
        if c == char: return pos

def format(number):
    length = len(number)
    f_number = float(number)
    point = getposition(str(f_number), '.')
    after_point = str(f_number)[point:]

    result = ""
    count = 0
    for i in number[point-1:0:-1]:
        if count == 3:
            result += ','
            count = 0
        result += i
        count += 1
    if count == 3:
        result += ','
    result += number[0]
    result = result[::-1]
    result += str(after_point)
    print(result)

if len(sys.argv) == 1:
    try:
        for line in sys.stdin:
            format(line.rstrip('\n'))
    except KeyboardInterrupt:
        exit(0)
else:
    for arg in sys.argv[1:]:
        format(arg)
