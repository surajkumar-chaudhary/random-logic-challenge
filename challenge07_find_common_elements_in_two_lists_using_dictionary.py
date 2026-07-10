list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]


lookup = {}
common = []
for n in list1:
    lookup[n] = True

for n in list2:
    if n in lookup and n not in common:
        common.append(n)

print(common)
