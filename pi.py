#!/usr/bin/python

from sys import argv

def pi_until(n):
    pi = 4 - 4/3
    t = 4
    m = 3
    for i in range(n):
        try:
            pi += (t/(m+2))-(t/(m+4))
            length = len(str(pi))+1
            #print(length*'\b', end="")
            print("\r{0}".format(pi), end="")
            m += 4
        except:
            print()
            exit()

if len(argv) >= 2: 
    pi_until(int(argv[1]))
    print()
else:
    pi_until(100000)
    print()
