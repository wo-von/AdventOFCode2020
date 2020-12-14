#!/usr/bin/python3
import sys

class Floor(object):
    def __init__(self, floorList):
        self.floorList = floorList
        self._rows = floorList.__len__()
        self._columns = floorList[0].__len__()
        self._tmp = list() # to hold the status of what needs to be done at a update
    @property
    def rows(self):
        return self._rows
    @property
    def columns(self):
        return self._columns
    def check_neighbours(self, i, j):
        '''
        i, j coordinates of the place
        returns 1 for change (empty with all neighbours empty)
        0 for no change (occupied with at least 4 neighbours occupied or floor)
        '''
        occupied = free = 0
        if self.floorList[i][j] == '.': # no change for floor
            return 0
        for iii in range(i - 1, i + 2):
            if iii >= self.rows or iii < 0:
                continue
            for jjj in range(j - 1, j + 2):
                if jjj >= self.columns or jjj < 0:
                    continue
                if iii == i and jjj == j:
                    continue
                if self.floorList[iii][jjj] == '.':
                    free += 1
                elif self.floorList[iii][jjj] == 'L':
                    free += 1
                else:
                    occupied += 1
        if self.floorList[i][j] == 'L' and occupied == 0:
            return 1
        elif self.floorList[i][j] == '#' and occupied >= 4:
            return 1
        else:
            return 0
    
    def check_update(self):
        '''
        Computes the possible rotations, if all zero, no update is possible and returns false
        otherwise true
        '''
        updatable = False
        self._tmp.clear()
        self._tmp = [ [0] * self.columns for i in range(self.rows) ]
        for i, row in enumerate(self.floorList):
            for j, seat in enumerate(row):
                if self.check_neighbours(i, j):
                    self._tmp[i][j] = 1
                    updatable = True
        return updatable
    
    def do_update(self):
        '''
        Should be called after check update, otherwise no update is done even if theoretically possible
        returns a new object, without modifying the current one
        '''
        new_floor_list = [ [0] * self.columns for i in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.columns):
                if self._tmp[i][j] == 1:
                    if self.floorList[i][j] == '#':
                        new_floor_list[i][j] = 'L'
                    else:
                        new_floor_list[i][j] = '#'
                else:
                    new_floor_list[i][j] = self.floorList[i][j]
        return Floor(new_floor_list)
    @property
    def countOccupied(self):
        _count = 0
        for row in self.floorList:
            _count += row.count('#')
        return _count
    # Special methods
    def __eq__(self, floorObj):
        if self.rows != floorObj.rows or self.columns != floorObj.columns:
            return False
        else:
            for i in range(self.rows):
                for j in range(self.columns):
                    if self.floorList[i][j] != floorObj.floorList[i][j]:
                        return False
                return True
   
    def __str__(self):
        toPrint = str()
        for row in self.floorList:
            toPrint += ''.join(row)
            toPrint += '\n'
        return toPrint[:-1]

Class practicalFloor(Floor):

def read_input(filename):
    f = open(filename)
    empty_floor = f.read()
    f.close()
    emptyFloorList = [ list(e) for e in empty_floor.split('\n') if e != '']
    return emptyFloorList


if len(sys.argv) == 2:
    input_file = sys.argv[1]
else:
    # so that it can be debugged in VS Code
    input_file = "11/input.txt"

initialfloorList = read_input(input_file)
# list of Floor objects as long as there is a shuffle to be done
initialFloor = Floor(initialfloorList)
tmpFloor = initialFloor
floorList = [initialFloor]

# Assuming at least one shuffle is possible
while True:
    if (floorList[-1].check_update()):
        tmpFloor = floorList[-1].do_update()
        floorList.append(tmpFloor)
    else:
        break
print(floorList[-1].countOccupied)