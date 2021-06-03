#!/bin/python
###program1
# a=[1 ,5 ,3, 6]
# b=[7, 15, 10, 9, 50, 40]
# c = a + b
# c.sort()
# print(c)


###program2
###method1
result = []
myarr = [17, 1, 3, 9, 10, 6]
for i in range(0, len(myarr) -1):
    for j in range(i+1, len(myarr)):
        if myarr[i] > myarr[j]:
            continue
        elif myarr[i] <= myarr[j]:
            break
    if j == len(myarr) - 1:
        result = result + [myarr[i]]
result = result + [myarr[len(myarr) - 1]]
print(result)

###method2
myarr = [17, 1, 3, 9, 10, 6]
result = []
result = result + [myarr[-1]]
max_value = myarr[-1]
for i in range(len(myarr)-1, -1, -1):
    if myarr[i] > max_value:
        max_value = myarr[i]
        result = result + [myarr[i]]
print(result)