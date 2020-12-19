#!/usr//bin/python3

import string

# We will hold the rules in a dictionary in following form:
# Key: rule number Value: list of strings of other sub rules
# messages in a list of strings
nodes = dict()
messages = list()
destinations = list()

with open("/home/ssh/Personal/adventOfCode2020/19/input-little.txt") as f:
    for line in f:
        if line[0] not in string.digits:
            break
        line = line.split(':')
        line[1] = line[1].strip()
        if line[1][0] == '"':
            nodes[int(line[0])] = line[1][1]
        else:
            line[1] = line[1].strip().split()
            try:
                index = line[1].index("|")
                dictvalue = [ [int(e) for e in line[1][:index] ], [ int(e) for e in line[1][index + 1:] ] ]
            except ValueError:
                dictvalue =  [[ int(e) for e in line[1] ]]
            nodes[int(line[0])] = dictvalue
            # rules[int(line[0])] = ["".join(e.strip()) for e in line[1].strip().split("|")]
    for line in f:
        messages.append(line.strip())


# populate a list of nodes that are destination 
# i.e. the value of dict entry is a single ascii letter
for node in nodes:
    if type(nodes[node]) == str:
        destinations.append(node)

def get_path(source, path = []):
    '''
    finds all paths from current souce (which is a node in nodes)
    to one of the destinations
    '''
    for member in nodes[source]:
        tmp = list()
        for rule in member:
            if rule in destinations:
                tmp.append(nodes[rule])
            else:
                tmp.append(get_path(rule, []))
        path.append(tmp)
    return path

paths = get_path(0, [])