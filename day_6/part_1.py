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
    
    time_blocks = []
    while True:
        i, j = guard
        if direction == '^':
            if [i - 1, j] in blocked:
                direction = '>'
            elif i - 1 < 0:
                if [i, j] not in visited:
                    visited.append([i, j])
                break
            else:
                if [i, j] not in visited:
                    visited.append([i, j])
                guard[0] -= 1
        elif direction == '>':
            if [i, j + 1] in blocked:
                direction = 'v'
            elif j + 1 >= width:
                if [i, j] not in visited:
                    visited.append([i, j])
                break
            else:
                if [i, j] not in visited:
                    visited.append([i, j])
                guard[1] += 1
        elif direction == 'v':
            if [i + 1, j] in blocked:
                direction = '<'
            elif i + 1 > height:
                if [i, j] not in visited:
                    visited.append([i, j])
                break
            else:
                if [i, j] not in visited:
                    visited.append([i, j])
                guard[0] += 1
        elif direction == '<':
            if [i, j - 1] in blocked:
                direction = '^'
            elif j - 1 < 0:
                if [i, j] not in visited:
                    visited.append([i, j])
                break
            else:
                if [i, j] not in visited:
                    visited.append([i, j])
                guard[1] -= 1
        else:
            print(direction, guard, 'IMPOSSIBLE')
            exit()

print(len(visited))