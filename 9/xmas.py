#!/usr/bin/python3

PREAMBEL_LENGTH = 25

def error_detector(candidate, preamble):
    preamble.sort()
    max = preamble[-1] + preamble[-2]
    min  = preamble[0] + preamble[1]
    # simple check to see if it is even in the possible range
    if candidate < min or candidate > max:
        return False
    # A Matrix, and skipping diagonal and lower half of it
    for i in range(PREAMBEL_LENGTH):
        for j in range(PREAMBEL_LENGTH):
            if i == j or j < i:
                continue
            if preamble[i] + preamble[j] == candidate:
                return True
    return False

def find_contiguous(flag, input, candidate):
    # all the way to the problematic input
    for sweeper in range(len(input[:flag])):
        sum = 0
        sub_list_flag = sweeper
        while sum <= candidate and sub_list_flag < flag:
            if sum == candidate:
                return input[sweeper: sub_list_flag]
            sum += input[sub_list_flag]
            sub_list_flag += 1

def main():
    
    problemexists = False
    preambleList = list()
    inputList = list()
    # Read the input into a list
    with open("input.txt") as f:
        for line in f:
            inputList.append(int(line.strip()))
    
    preambleList = inputList[:25]

    for flag in range(25, len(inputList)):
        candidate = inputList[flag]
        if not error_detector(candidate, preambleList):
            problemexists = True
            break
        flag += 1
        preambleList = inputList[flag - 25:flag]

    if problemexists:
        otherSum = find_contiguous(flag, inputList, candidate)
        otherSum.sort()
        weakness = otherSum[0] + otherSum[-1] 
        print(weakness)

if __name__=="__main__":
    main()
