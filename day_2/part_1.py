import math

source = 'day_2\\input.txt'

data = open(source).read()   

lines = data.split('\n')
reports = [[int(level) for level in report.split(' ')] for report in lines]
differences = [[levels[i+ 1] - level for i,level in enumerate(levels[:-1])] for levels in reports]

safe = [[(difference[0] > 0) == (diff > 0) and abs(diff) <= 3 and abs(diff) >= 1 for diff in difference] for difference in differences]

print(sum([1 if False not in s else 0 for s in safe]))