source = 'day_5\\input.txt'

data = open(source).read()

rules, queues = data.split('\n\n')
rules = [rule.split('|') for rule in rules.split('\n')]

pages = {}
for first, second in rules:
    if first not in pages.keys():
        pages[first] = {
            "before": [],
            "after": [second]
            }
    else:
        pages[first]["after"].append(second)
    if second not in pages.keys():
        pages[second] = {
            "before": [first],
            "after": []
            }
    else:
        pages[second]["before"].append(first)
            
queues = [queue.split(',') for queue in queues.split('\n')]

bad = []
for i, queue in enumerate(queues):
    for j, page in enumerate(queue):
        before = queue[:j]
        after = queue[j + 1:]
        for b in before:
            if b in pages[page]["after"]:
                if queue not in bad:
                    bad.append(queue)
                break
        for a in after:
            if a in pages[page]["before"]:
                if queue not in bad:
                    bad.append(queue)
                break

sum = 0


for queue in queues:
    if queue not in bad:
        sum += int(queue[(len(queue) - 1) // 2])
print(sum)

print()


        