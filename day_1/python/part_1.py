source = 'day_1\\input.txt'

list1 = []
list2 = []
for line in open(source).readlines():
    list1.append(int(line.strip('\n').split('   ')[0]))
    list2.append(int(line.strip('\n').split('   ')[1]))
list1.sort()
list2.sort()

sum = 0
for i in range(len(list1)):
    sum += max(list1[i], list2[i]) - min(list1[i], list2[i])
print(sum)