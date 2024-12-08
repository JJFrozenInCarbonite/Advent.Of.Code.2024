import copy

source = 'day_6\\input.txt'

def findGuard(data):
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            if col in ['^', '>', 'v,' '<']:
                return data, col, i, j
            

def getNextTile(data: list, dir: str, i: int, j: int):
    if dir == '^':
        if i > 0:
            if data[i - 1][j] == '#':
                return getNextTile(data, '>', i, j)
            else:
                i -= 1
        else:
            dir = 'F'
    elif dir == '>':
        if j < len(data[0]) - 1:
            if data[i][j + 1] == '#':
                return getNextTile(data, 'v', i, j)
            else:
                j += 1
        else:
            dir = 'F'
    elif dir == 'v':
        if i < len(data) - 1:
            if data[i + 1][j] == '#':
                return getNextTile(data, '<', i, j)
            else:
                i += 1
        else:
            dir = 'F'
    elif dir == '<':
        if j > 0:
            if data[i][j - 1] == '#':
                return getNextTile(data, '^', i, j)
            else:
                j -= 1
        else:
            dir = 'F'
    else:
        print("NOT POSSIBLE")
        exit(1)

    return data, dir, i, j


if __name__ == '__main__':
    data = open(source).read()

    data = [[char for char in row] for row in data.split('\n')]
    
    data, direction, i, j = findGuard(data)
    path = []
    while direction != 'F':
        if [i, j] not in path:
            path.append([i, j])
        data, direction, i, j = getNextTile(data, direction, i, j)
        
    new_paths = []
    looped_path = []
    k = 0
    for i, j in path:
        k += 1
        if [i, j] == path[0]:
            continue
        new_data = copy.deepcopy(data)
        new_data[i][j] = '#'
        guard_i, guard_j = path[0]
        guard_direction = data[guard_i][guard_j]
        new_path = []
        while guard_direction != 'F':
            new_path.append([guard_direction, guard_i, guard_j])
            new_data, guard_direction, guard_i, guard_j = getNextTile(new_data, guard_direction, guard_i, guard_j)
            print(k, guard_direction, guard_i, guard_j)
            if [guard_direction, guard_i, guard_j] in new_path:
                looped_path.append(new_path)
                print(new_path)
                break
            # new_path.append([guard_direction,  guard_i, guard_j])
    
    print(len(looped_path))
        
        
"""         new_data = copy.deepcopy(data)
        new_data[i][j] = '#'
        new_path = []
        new_direction = new_data[path[0][0]][path[0][1]]
        while new_direction != 'F':
            if[new_direction, i, j] not in new_path:
                new_path.append([direction, i, j])
            else:
                print('hello')
                new_path.append([new_direction, i, j])
                new_paths.append(new_path)
                blocked_paths.append(new_path)
                blocked += 1
        
                break
            new_data, new_direction, i, j = getNextTile(new_data, new_direction, i, j)
            if new_direction == 'F':
                unblocked += 1


            
        
    print(len(blocked_paths))
    print(blocked)
    print(unblocked)
 """

    
        
    



