# two wires connected to central port extended to grid
# trace path of each wire, one wire per line of text (input)
# wires occasionally cross path
# Find intersection point closest to central 
# Manhattan distance for measurement

import numpy as np

x = [1, 3, 5]
y = [5, 3, 1]


def manhattan(x, y):
    return sum(abs(np.subtract(x, y)))

x = np.zeros(shape = (12, 12))
o = (1, 1)

x[10-1][1] = 3

test_text = ['R75','D30','R83','U83', 'L12','D49','R71','U7','L72'
'U62','R66','U55','R34','D71','R55','D58','R83']

test_text = ['R8','U5','L5','D3']
know_current_direction_row = 10 - 1
know_current_direction_column = 1

print(x)
print('column',know_current_direction_column)
print('row',know_current_direction_row)

direction = test_text[0][0]
print(direction)
length = int(test_text[0].replace(direction, ''))
print(length)
if direction == "R":
    x[know_current_direction_row, know_current_direction_column+1:know_current_direction_column + length] = 1
    x[know_current_direction_row, know_current_direction_column + length] = 2
    know_current_direction_column = know_current_direction_column + length
if direction == "L":
    x[know_current_direction_row, know_current_direction_column+1:know_current_direction_column - length] = 1
    know_current_direction_column = know_current_direction_column - length
if direction == "U":
    x[know_current_direction_row:know_current_direction_row - length, know_current_direction_column] = 1
    x[know_current_direction_row - length, know_current_direction_column] = 2
    know_current_direction_row = know_current_direction_row + length
if direction == "D":
    x[know_current_direction_row:know_current_direction_row + length, know_current_direction_column] = 1
    x[know_current_direction_row + length, know_current_direction_column] = 2
    know_current_direction_row = know_current_direction_row - length


print(x)
print('column', know_current_direction_column)
print('row',know_current_direction_row)

direction = test_text[1][0]
print(direction)
length = int(test_text[1].replace(direction, ''))
print(length)
if direction == "R":
    x[know_current_direction_row, know_current_direction_column+1:know_current_direction_column + length] = 1
    x[know_current_direction_row, know_current_direction_column + length] = 2
    know_current_direction_column = know_current_direction_column + length
if direction == "L":
    x[know_current_direction_row, know_current_direction_column+1:know_current_direction_column - length] = 1
    know_current_direction_column = know_current_direction_column - length
if direction == "U":
    x[know_current_direction_row:know_current_direction_row - length, know_current_direction_column] = 1
    x[know_current_direction_row - length, know_current_direction_column] = 2
    know_current_direction_row = know_current_direction_row + length
if direction == "D":
    x[know_current_direction_row:know_current_direction_row + length, know_current_direction_column] = 1
    x[know_current_direction_row + length, know_current_direction_column] = 2
    know_current_direction_row = know_current_direction_row - length


print(x)
print('column',know_current_direction_column)
print('row',know_current_direction_row)