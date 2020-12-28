#!/usr/bin/python3

f = open("/home/sina/Learning/adventOfCode/AdventOFCode2020/2/input-2.txt")
inputraw = f.read()
f.close()

inputlist = inputraw.split('\n')

inputlist = inputlist[:-1]
processedinput = [ s.split(': ') for s in inputlist ]

wrong_count = 0

for password in processedinput:
    if password[1].count(password[0].split(' ')[1]) < int(password[0].split(' ')[0].split('-')[0]) or password[1].count(password[0].split(' ')[1]) > int(password[0].split(' ')[0].split('-')[1]):
        wrong_count += 1

print("Part1: valid number of passwords is",len(processedinput) - wrong_count)

part2_correct_count = 0

for password in processedinput:
    counter = 0
    try:
        if password[1][int(password[0].split(' ')[0].split('-')[0]) - 1] == password[0].split(' ')[1]:
            counter += 1
        if password[1][int(password[0].split(' ')[0].split('-')[1]) - 1] == password[0].split(' ')[1]:
            counter += 1
    except IndexError:
        pass
    if counter == 1:
        part2_correct_count += 1

print("part2: valid number of passwords is", part2_correct_count)