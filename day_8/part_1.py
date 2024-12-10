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
    
    input("Start Antinode Analysis")
    antinodes = []
    for a, frequency in enumerate(antennas.keys()):
        print(f"{a} of {len(antennas.keys())} Freq: {frequency}")
        for i, antenna_1 in enumerate(antennas[frequency][:-1]):
            for antenna_2 in antennas[frequency][i + 1:]:
                x1, y1 = convert_to_x_y(antenna_1, width, height)
                x2, y2 = convert_to_x_y(antenna_2, width, height)
                dx = x2 - x1
                dy = y2 - y1

                print(f"  Testing: {antenna_1}, {antenna_2}")
                print(f"    (x, y) ({x1}, {y1}), ({x2}, {y2})")
                print(f"    (i, j) {convert_to_i_j((x1, y1), width, height)}")
                a1 = (x1 - dx, y1 - dy)
                a2 = (x2 + dx, y2 + dy)

                if a1[0] >= 0 and a1[0] < width and a1[1] >= 0 and a1[1] < height:
                    a1_ij = convert_to_i_j(a1, width, height)
                    print(f"    Antinode 1: (x,y) {a1}, (i,j) {a1_ij}")
                    if a1_ij not in antinodes:
                        antinodes.append(tuple(a1_ij))
                if a2[0] >= 0 and a2[0] < width and a2[1] >= 0 and a2[1] < height:
                    a2_ij = convert_to_i_j(a2, width, height)
                    print(f"    Antinode 2: (x,y) {a2}, (i,j) {a2_ij}")
                    if a2_ij not in antinodes:
                        antinodes.append(tuple(a2_ij))
            
    print(antinodes)
    print(len(antinodes))