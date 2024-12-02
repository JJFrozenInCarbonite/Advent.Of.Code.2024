import pandas as pd

source = 'day_1\\input.txt'

list1 = []
list2 = []
for line in open(source).readlines():
    var1 = int(line.strip('\n').split('   ')[0])
    if var1 not in list1:
        list1.append(var1)
    list2.append(int(line.strip('\n').split('   ')[1]))

list3 = []
for l1 in list1:
    total = 0
    for l2 in  list2:
        if l1 == l2:
            total += l1
    list3.append(total)
        
print(sum(list3))