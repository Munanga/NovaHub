def split(arr, size):
    arrs = []
    while len(arr) > size:
        pice = arr[:size]
        arrs.append(pice)
        arr = arr[size:]
    arrs.append(arr)
    return arrs

x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
lists = split(x, 5)
for list in lists:
    print(list)