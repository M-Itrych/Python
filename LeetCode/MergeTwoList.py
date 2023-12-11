def partition(arr, p, r):
    pivot = arr[p]
    left = p - 1
    right = r + 1
    for i in range(3):
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right += 1
        if left < right:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
        else:
            break

    return right

def quickSort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quickSort(arr, p, q)
        quickSort(arr, q+1, r)



def mergeTwoLists(list1, list2):
    newList = list1 + list2
    return quickSort(newList, 0, len(newList)-1)








list1 = [1,2,4]
list2 = [1,3,4]

mergeTwoLists(list1, list2)