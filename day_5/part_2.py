import copy

source = 'day_5\\input.txt'

data = open(source).read()

rules, queues = data.split('\n\n')

bad = []
good = []
fixed = []
for queue in queues.split('\n'):
    pages = queue.split(',')
    for i, page in enumerate(pages[:-1]):
        if rules.find(f'{pages[i + 1]}|{page}') != -1:
            if queue not in bad:
                bad.append(queue)
    if queue not in bad:
        good.append(queue)

sum = 0
for g in good:
    pages = g.split(',')
    sum += int(pages[(len(pages) - 1) // 2])


for queue in bad:
    pages = queue.split(',')
    i = 0
    while True:
        if i < len(pages) - 1:
            if rules.find(f'{pages[i + 1]}|{pages[i]}') != -1:
                temp = pages[i]
                pages[i] = pages[i + 1]
                pages[i + 1] = temp
                i = 0
            else:
                i += 1
        else:
            break
    fixed.append(pages)

sum = 0
for f in fixed:
    sum += int(f[(len(f) - 1) // 2])
print(sum)