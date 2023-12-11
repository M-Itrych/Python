#https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

def findSpecialInteger(arr):
    table = {}
    count = 1
    for el in arr:
        if el in table:
            count += 1
        table[el] = count
        count = 0

    return table


print(findSpecialInteger([1,2,2,6,6,6,6,7,10]))