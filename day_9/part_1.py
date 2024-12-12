import copy
import os

source =  os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt')     

if __name__ == '__main__':
    data = open(source).read()
    data = [int(char) for char in data]
    
    unsorted = []
    i = 0
    for j, num in enumerate(data):
        print(f'Processing: i: {i}, j: {j}, length: {len(data)}')
        if j % 2 == 0:
            to_append = i
            i += 1
        else:
            to_append = '.'
        for k in range(0, num):
            unsorted.append(to_append)

    
    sorted = copy.deepcopy(unsorted)
    
    i = 0
    j = len(sorted) - 1
    while i < j - 1:
        while unsorted[i] != '.':
            i += 1
        while unsorted[j] == '.':
            j -= 1
        if j < i:
            break
        print(f'Sorting: i: {i}, j: {j}, length: {len(unsorted)}, unsorted[i]: {unsorted[i]}, unsorted[j]: {unsorted[j]}')
        sorted[i] = unsorted[j]
        sorted[j] = '.'
        i += 1
        j -= 1
    
    with open('sorted.txt', 'w') as f:
        for ele in sorted:
            f.write(str(ele))

    total = 0
    for i, num in enumerate(sorted):
        print(f"Checksum Step: i: {i}, length: {len(sorted)}")
        if num == '.':
            break
        else:
            total += (num * i)
    
    print(total)

        