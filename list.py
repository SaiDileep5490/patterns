list1 = [1,5,5,3,8,2,1,6]
list2 = ['s','a','i']
list3 = ["Sai got ",'A',"grade","marks =",98]


list4 = list2+list3
print(list4)

print(list3[0:2])

print(list1[-4:-1])

print(list1[:7])

print(list1[0: ])

print(list1[:])

list1.append(7)
print(list1)

list1.insert(4,9)
print(list1)

list1.extend(list2)
print(list1)

list1.pop(2)
print(list1)


list1.copy()
print(list1)
