from collections import Counter

# TEST 1
list1 = []
list2 = []

with open("./data.txt", 'r') as ids:
	for id in ids:
		lists = id.split()
		intlists = list(map(int, lists))

		list1.append(intlists[0])
		list2.append(intlists[1])

# list1 = sorted(list1)
# list2 = sorted(list2)

# iter = 0
# distance = []
# for l1 in range(0 , len(list1)):
#     distance.append(abs(int(list1[l1]) - int(list2[l1])))

# print(sum(distance))

# Total distance: 1580061

# TEST 2
min_list1 = [3,4,2,1,3,3]
min_list2 = [4,3,5,3,9,3]

result = []
for l1 in list1:
	similarity_score = list2.count(l1)
	
	result.append(l1 * similarity_score)

print(sum(result))

# Similarity score: 23046913