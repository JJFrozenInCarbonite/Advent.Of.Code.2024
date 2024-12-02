import copy

source = 'day_2\\input.txt'

def check(list: list):
    slope = list[0] - list[1]
    if slope == 0:
        return False
    for i, l in enumerate(list[:-1]):
        difference = l - list[i + 1]
        if abs(difference) > 3 or abs(difference) < 1:
            return False
        if (slope > 0 and difference < 0) or (slope < 0 and difference > 0) or difference == 0:
            return False
    return True
        

data = open(source).read().split('\n')
reports = [[int(level) for level in  levels.split(' ')]  for levels in data]

safe_count = 0
for levels in reports:
    if check(levels):
        safe_count += 1
    else:
        for i in range(len(levels)):
            new_levels = copy.deepcopy(levels)
            new_levels.pop(i)
            if check(new_levels):
                safe_count += 1
                break
print(safe_count)