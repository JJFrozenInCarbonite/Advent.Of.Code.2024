source = 'day_4\\input.txt'

data = open(source).read().split('\n')
xmas = []
for i, row in enumerate(data):
    for j, char in enumerate(row):
        if j <= len(row) - 4:
            xmas.append(row[j:j+4])
        if i <= len(data) - 4:
            string = ''
            for k in range(0, 4):
                string += data[i + k][j]
            xmas.append(string)
        if i <= len(data) - 4 and j <= len(row) - 4:
            string = ''
            for k in range(0, 4):
                string += data[i + k][j + k]
            xmas.append(string)
        if i >= 3 and j <= len(row) - 4:
            string = ''
            for k in range(0, 4):
                string += data[i - k][j + k]
            xmas.append(string)
count = 0
for x in xmas:
    if x == 'XMAS' or x == 'SAMX':
        count += 1
print(count)