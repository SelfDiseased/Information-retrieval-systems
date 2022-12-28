def common(list1, list2):
    load1 = set(list1)
    load2 = set(list2)
    if len(load1.intersection(load2)) > 0:
        return list(load1.intersection(load2)) 
    else:
        return []

l1 = ['a', 'b', 'c']
l2 = ['c', 'a', 'z']
l3 = ['x', 'y', 'z']
l4 = ['a', 'a', 'b']
l5 = ['x', 'a', 'a']

print(l1, l2)
print(common(l1, l2))

print(l1, l3)
print(common(l1, l3))

print(l4, l5)
print(common(l4, l5))