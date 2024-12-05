import math

list1 = []
list2 = []

with open("./locationIDs.txt", 'r') as ids:
	for id in ids:
		lists = id.split()

		list1.append(lists[0])
		list2.append(lists[1])

list1 = sorted(list1)
list2 = sorted(list2)

iter = 0
distance = []
for l1 in range(0 , len(list1)):
    distance.append(abs(int(list1[l1]) - int(list2[l1])))

print(sum(distance))