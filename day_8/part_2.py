import math
import os

source =  os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt')     

def convert_to_x_y(pair, width, height):
    i, j = pair
    return j, height - i - 1,

def convert_to_i_j(pair, width, height):
    x, y = pair
    return height - y - 1, x



if __name__ == '__main__':
    data = open(source).read()
    data = data.split('\n')


    height = len(data)
    width = len(data[0])

    antennas = {}
    for i, line in enumerate(data):
        for j, col in enumerate(line):
            if col != '.':
                if col not in antennas.keys():
                    antennas[col] = [(i,j)]
                else:
                    temp = list(antennas[col])
                    temp.append((i,j))
                    antennas[col] = temp
    
    antinodes = []
    for a, frequency in enumerate(antennas.keys()):
        print(f"{a} of {len(antennas.keys())} Freq: {frequency}")
        for i, antenna_1 in enumerate(antennas[frequency][:-1]):
            if antenna_1 not in antinodes:
                antinodes.append(antenna_1)
            for antenna_2 in antennas[frequency][i + 1:]:
                if antenna_2 not in antinodes:
                    antinodes.append(antenna_2)
                x1, y1 = convert_to_x_y(antenna_1, width, height)
                x2, y2 = convert_to_x_y(antenna_2, width, height)
                dx = x2 - x1
                dy = y2 - y1

                print(f"  Testing: {antenna_1}, {antenna_2}")
                print(f"    (x, y) ({x1}, {y1}), ({x2}, {y2})")
                print(f"    (i, j) {convert_to_i_j((x1, y1), width, height)}")
                a1 = (x1 - dx, y1 - dy)
                a2 = (x2 + dx, y2 + dy)

                ax = x1
                ay = y1
                while True:
                    ax = ax - dx
                    ay = ay - dy
                    if ax >= 0 and ax < width and ay >= 0 and ay < height:
                        antinode = convert_to_i_j((ax, ay), width, height)
                        if antinode not in antinodes:
                            antinodes.append(antinode)
                    else:
                        break

                ax = x2
                ay = y2
                while True:
                    ax = ax + dx
                    ay = ay + dy
                    if ax >= 0 and ax < width and ay >= 0 and ay < height:
                        antinode = convert_to_i_j((ax, ay), width, height)
                        if antinode not in antinodes:
                            antinodes.append(antinode)
                    else:
                        break

            
    print(antinodes)
    print(len(antinodes))