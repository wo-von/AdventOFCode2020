#!/usr/bin/python3
import copy

def add_rims(lst):
    '''
    gets a plate, and checks if there should be rims around it
    '''
    left = right = top = bottom = False
    for row in lst:
        if row[0] == '#': # This part is not efficient enough
            left |= True
        if row[-1] == '#':
            right |= True
        if left == True and right == True:
            break
    
    expanded = [ ['.'] * left + row[:] + ["."] * right for row in lst]
    empty_row = ["." for _ in range(len(expanded[0]))]
    
    if "#" in expanded[0]:
        expanded.insert(0, copy.deepcopy(empty_row))
    if "#" in expanded[-1]:
        expanded.append(copy.deepcopy(empty_row))
    return expanded

def add_dimension(space):
    '''
    input is a space (a list of plates)
    expands the dimensions, if needed
    '''
    empty_plate = [ ["." for _ in range(len(space[0][0]))] for _ in range(len(space[0])) ]

    for row in space[0]: # bottom plate
        if '#' in row:
            space.insert(0, empty_plate)
            break
    for row in space[-1]:
        if '#' in row:
            space.append(empty_plate)
            break
    return space

def check_active_neighbours(x, y, z, dimension: list, space):
    '''
    checks how many of the naeighbours are active
    '''
    numactive = 0
    for zz in range(z-1, z+2):
        if zz < 0 or zz >= dimension[2]:
            continue
        for  yy in range(y-1, y+2):
            if yy < 0 or yy >= dimension[1]:
                continue
            for xx in range(x-1, x+2):
                if xx < 0 or xx >= dimension[0]:
                    continue
                if xx == x and yy == y and zz == z:
                    continue
                if space[zz][yy][xx] == "#":
                    numactive += 1
    return numactive

def dimension(space):
    '''
    gets an space and return a list of its dimension
    [x, y, z]
    '''
    return [len(space[0][0]), len(space[0]), len(space)]

def take_step(space):
    '''
    sweeps the whole space, toggles each cell
        - If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
        - If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
    '''
    spaceCopy = copy.deepcopy(space)
    for z, plate in enumerate(spaceCopy):
        for y, row in enumerate(plate):
            for x, cell in enumerate(row):
                num_active = check_active_neighbours(x, y, z, dimension(space), spaceCopy)
                if cell == "#" and (num_active != 2 and num_active != 3):
                    space[z][y][x] = "."
                elif cell == "." and num_active == 3:
                    space[z][y][x] = "#"
    return space                

def active_counter(space):
    num_active = 0
    for plate in space:
        for row in plate:
            for cell in row:
                if cell == "#":
                    num_active += 1
    return num_active

f = open("input-small")
initialString = f.read()
f.close()
initialList = [list(x) for x in initialString.split() if x != '']

firststage = add_rims(initialList)

empty_plate = [ ["." for _ in range(len(firststage[0]))] for _ in range(len(firststage)) ]
initialSpace = [empty_plate, firststage, empty_plate]
start = copy.deepcopy(initialSpace)
startspacetest = add_rims()
