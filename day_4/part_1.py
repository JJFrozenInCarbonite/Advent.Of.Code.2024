source = 'day_4\\input.txt'

def vertStrings(data: list, h, w):
    strings = []
    
    for i in range(0, w):
        string = ''
        for j in range(0, h):
            string += data[j][i]
        strings.append(string)
    return strings
        
def xStrings(data: list, h, w):
    strings = []

    for i in range(0, h):
        string = ''
        for j in range(0, i + 1):
            a = h - i - j - 1
            b = w - j - 1
            #print(f"({a}, {b}), ", end='')
            #print(data[i - j][j], end='')
            #print(10 - i, 10 - j, end=' ')
            print(data[b][a], end='')
            #print(data[9 - j][9 - i], end='')
        print()

            

def new(data: list, h, w):
    strings = []
    for i in range(h - 1, -1, -1):
        for j in range(0, w - 1):
            a = i
            b = j
            print(f'({a}, {b})', end = '')
        print()




if __name__ == '__main__':
    data = open(source).read().split('\n')
    height = len(data)
    width = len(data[0])

    

    strings = data
    strings.extend(vertStrings(data, height, width))
    #xStrings(data, height, width)
    new(data, height, width)

    print(strings)

    #print(strings)
    #print(get_vertical_strings(rows))
    


    


# row start: 3, 7 | 3, len(row) - 3
# column start: 3, 7 | 3, len(column) - 3
