import math

list1 = []
list2 = []

with open("./data.txt", 'r') as ids:
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

# print(sum(distance))

# Total distance: 1580061

# Test 2
result = []
for l1 in list1:
	if l1 in list2:
		for l2 in list2:
			if l1 == l2:
				print(int(l1) + int(l2))