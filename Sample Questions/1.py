def subsetA(arr):
    max1 = max(arr)
    arr.remove(max1)

    max2 = max(arr)
    arr.remove(max2)

    listA = [max1, max2]

    while sum(listA) < sum(arr):
        listA.append(max(arr))
        arr.remove(max(arr))

    # sort and return the result
    print(sorted(listA))


arr = [6, 5, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
subsetA(arr)
