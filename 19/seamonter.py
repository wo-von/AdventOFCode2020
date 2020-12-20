#!/usr//bin/python3

import string

# We will hold the rules in a dictionary in following form:
# Key: rule number Value: list of strings of other sub rules
# messages in a list of strings
rules = dict()
messages = list()
destinations = list()

with open("/home/ssh/Personal/adventOfCode2020/19/input-little.txt") as f:
    for line in f:
        if line[0] not in string.digits:
            break
        line = line.split(':')
        line[1] = line[1].strip()
        if line[1][0] == '"':
            rules[int(line[0])] = line[1][1]
        else:
            line[1] = line[1].strip().split()
            try:
                index = line[1].index("|")
                dictvalue = [ [int(e) for e in line[1][:index] ], [ int(e) for e in line[1][index + 1:] ] ]
            except ValueError:
                dictvalue =  [[ int(e) for e in line[1] ]]
            rules[int(line[0])] = dictvalue
            # rules[int(line[0])] = ["".join(e.strip()) for e in line[1].strip().split("|")]
    for line in f:
        messages.append(line.strip())


# populate a list of nodes that are destination 
# i.e. the value of dict entry is a single ascii letter
for rule in rules:
    if type(rules[rule]) == str:
        destinations.append(rule)

def get_path(source):
    '''
    Translate a set of rules into its literal counterpart
    '''
    path = []
    for member in rules[source]:
        tmp = list()
        for rule in member:
            if rule in destinations:
                tmp.append(rules[rule])
            else:
                tmp.append(get_path(rule))
        path.append(tmp)
    return path

paths = get_path(0)

def check_message(message, paths):
    '''
    Check if a message is in accordance with rule 0 (and its expansion)
    '''
    checksout = False
    for path in paths:
        if isinstance(path, list):
            if any([isinstance(e, list) for e in path]):
                checksout |= check_message(message, path)
                if checksout == False:
                    break
            else:
                if message[:"".join(path).__len__()] == "".join(path):
                    if len(message["".join(path).__len__():]) == 0:
                        return True
                    else:
                        checksout |= check_message(message["".join(path).__len__():], path)
                else:
                    return False
        else: # Then it is a standalone string, just check it          
            if message[0] == path:
                checksout |= check_message(message[1:], path)
            else:
                return False
    return checksout

total_wrong = 0

for message in messages:
    if not check_message(message, paths):
        total_wrong += 1

print("total wrong messages:", total_wrong)