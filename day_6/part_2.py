import copy

source = 'day_6\\input.txt'

if __name__ == '__main__':
    data = open(source).read()


    blocked = []
    guard = []
    visited = []
    direction = ''

    grid = [[char for char in row] for row in data.split('\n')]
    
    height = len(grid)
    width = len(grid[0])

    i = j = 0
    while True:
        char = grid[i][j]
        if char == '^':
            guard = [i,j]
            direction = char
        elif char == 'v':
            guard = [i, j]
            direction = char
        elif char == '>':
            guard = [i, j]
            direction = char
        elif char == '<':
            guard = [i, j]
            direction = char
        if char == '#':
            blocked.append([i,j])
        if i < width - 1:
            i += 1
        else:
            if j < height - 1:
                i = 0
                j += 1
            else:
                break
    
