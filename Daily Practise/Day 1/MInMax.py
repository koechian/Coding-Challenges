# sort it in place and pick the 1st 4 elements to form the lowest sum and the last 4 to form the largest sum


def minmax(arr):
    arr.sort()

    largest = arr[-4:]
    smallest = arr[:4]

    print(str(sum(smallest)) + " " + str(sum(largest)))


arr = [1, 5, 3, 7, 9]
# 1, 3, 5, 7, 9
minmax(arr)
