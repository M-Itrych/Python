def array_diff(a, b):
    new_arr = []
    for i, el in enumerate(a):
        if el in b:
            new_arr.append(el)
    return new_arr


print(array_diff([1,2,2], [2]))