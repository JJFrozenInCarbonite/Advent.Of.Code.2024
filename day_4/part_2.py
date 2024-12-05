source = 'day_4\\input.txt'

data = open(source).read().split('\n')
count = 0
for i, row in enumerate(data):
    for j, char in enumerate(row):
        if char == 'A':
            if i >= 1 and i <= len(data) - 2 and j >= 1 and j <= len(row) - 2:
                string1 = data[i - 1][j - 1] + data[i + 1][j + 1]
                string2 = data[i - 1][j + 1] + data[i + 1][j - 1]
                if (string1 == 'MS' or string1 == 'SM') and (string2 == 'MS' or string2 == 'SM'):
                    count += 1
print(count)
