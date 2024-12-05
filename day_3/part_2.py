import re

source = 'day_3\\input.txt'

data = open(source).read()
data = data.split('do()')
data = ''.join([d.split("don't()")[0] for d in data])
data = sum([int(mult[4:-1].split(',')[0]) * int(mult[4:-1].split(',')[1]) for mult in re.findall('mul\\(\\d*,\\d*\\)', data)])

print(data)
