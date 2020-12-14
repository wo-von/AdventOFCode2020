#!/usr/bin/python3

def part1(cord):
    '''
    number of 1 diffs * number of 3 diffs
    '''
    diff = [ i - j for i, j in zip(cord[1:], cord[:-1])]
    return diff.count(1) * diff.count(3)

def read_input(filename):
    '''
    reads the input file into a list and sorts it
    adds 0 and max + 3 for outlet and device
    '''
    f = open(filename)
    joltages = f.read()
    f.close()

    joltages = [ int(e) for e in joltages.split('\n') if e != '' ]

    joltages.sort()

    return [0] + joltages + [joltages[-1] + 3]

# Simple DFS, since it is already sorted and there will be no loops as long as we go rising
def DFS(cord, start, end, counter):
    '''
    cord is the list of all adapter (graph) and also the outlet and device
    path is the arrangement that is being considered
    start and end are ints from cord
    '''
    if start == end:
        counter += 1
        return counter
    else:
        for children in [start + 1, start + 2, start + 3]:
            if children in cord:
                counter = DFS(cord, children, end, counter)
                print(counter)
            else:
                continue
    return counter

def main(filename):
    cord = read_input(filename)
    # List of all possible ways
    cords_count = DFS(cord, cord[0], cord[-1], 0)
    print(cords_count)


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        inputfile = "10/input-10-ex.txt" # used for debugging in VS Code
    else:
        inputfile = sys.argv[2]
    main(inputfile)


    