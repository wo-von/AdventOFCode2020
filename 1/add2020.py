#!/usr/bin/python3
import time
import itertools


with open("/home/sina/Learning/adventOfCode/AdventOFCode2020/1/input-1.txt") as f:
    inputlist = [ int(e) for e in f.read().split() ]

start = time.time()

for i, item1 in enumerate(inputlist[:-3]):
    for item2 in inputlist[i + 1 : -2]:
        for item3 in inputlist[i+2:]:
            if item1 + item2 + item3 == 2020:
                print(item1 * item2 * item3)
                break

end = time.time()

print("Stupid version needed", end - start)

start = time.time()

for item1, item2, item3 in itertools.combinations(inputlist, 3):
    if item1 + item2 + item3 == 2020:
        print(item1 * item2 * item3)
        break

end = time.time()

print("better version time is", end - start)


