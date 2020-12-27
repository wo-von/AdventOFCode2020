#!/usr/bin/python3

with open("/home/sina/Learning/adventOfCode/AdventOFCode2020/1/input-1.txt") as f:
    inputlist = [ int(e) for e in f.read().split() ]

max_allowabale = 2020 - min(inputlist)

for i, item in enumerate(inputlist):
    if item > max_allowabale:
        continue
    try:
        candidate = inputlist[inputlist.index(2020 - item)]
        print(candidate * item)
        break
    except ValueError:
        continue




