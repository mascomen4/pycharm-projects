#!usr/bin/env python3
#Copyright (c) Podmogilniy Ivan

''' Module description...'''

_grid = []
_max_rows = 25
_max_columns = 50
_char_template = ' '

class RangeError(Exception): pass
class RowRangeError(RangeError): pass
class ColumnRangeError(RangeError): pass

def resize(max_rows, max_columns, char = None):
    char = test_char(char)
    global _grid, _max_rows, _max_columns, _char_template
    _grid = [[char for i in range(max_columns)] for j in range(max_rows)]
    _max_rows = max_rows
    _max_columns = max_columns
    _char_template = char

def add_rectangle(row0, column0, row1, column1, char = None, fill = False):
    char = test_char(char)
    if fill == False:
        for row in (row0, row1):
            add_horizontal_line(row, column0, column1, char)
        for column in (column0, column1):
            add_vertical_line(column, row0, row1, char)
    else:
        for row in range(row0, row1):
            add_horizontal_line(row, column0, column1, char)

def add_horizontal_line(row, column0, column1, char = None):
    char = test_char(char)
    row, column0, column1 = row -1, column0 -1, column1 -1
    try:
        for c in range(column0, column1 +1):
            global _grid
            _grid[row][c] = char
            
    except IndexError:
        if 0 <= row < _max_rows:
            raise RowRangeError()
        raise ColumnRangeError()

def add_vertical_line(column, row0, row1, char = None):
    char = test_char(char)
    column, row0, row1 = column -1, row0 -1, row1 -1
    try:
        for row in range(row0, row1 +1):
            global _grid
            _grid[row][column] = char
            
    except IndexError:
        if 0 <= column < _max_columns:
            raise ColumnRangeError()
        raise RowRangeError()

def add_text(row, column, text, char = None):
    char  = test_char(char)
    row, column = row -1, column -1
    try:
        for item in range(column, column + len(text)):
            global _grid
            _grid[row][item] = text[item - column]
    except IndexError:
        if not 0 <= row <  _max_row:
            raise RowRangeError()
        raise ColumnRangeError()

def set_background(char = ' '):
    char = test_char(char)
    global _grid, _char_template
    for row_index, row in enumerate(_grid):
        for column_index, column in enumerate(row):
            if column in _char_template:
                _grid[row_index][column_index] = char

def char_at(row, column):
    row, column = row -1, column -1
    try:
        char =  _grid[row][column]
        return char
    except IndexError:
        if not 0 <= row < _max_row:
            raise RowRangeError()
        raise ColumnRangeError()

def get_size():
    return _max_rows, _max_columns
    
def test_char(char):
    char = ' ' if char is None else char
    assert len(char)==1, ("'char' length must be a single character, "
                          "{0} is too long".format(char))
    return char

def render():
    for row in _grid:
        for c in row:
            print(c, end = '')
        print()
        
resize(_max_rows, _max_columns)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
