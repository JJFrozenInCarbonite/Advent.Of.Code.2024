import re

source = 'day_3\\input.txt'

data = open(source).read()
data = sum([int(mult[4:-1].split(',')[0]) * int(mult[4:-1].split(',')[1]) for mult in re.findall('mul\\(\\d*,\\d*\\)', data)])

print(data)
