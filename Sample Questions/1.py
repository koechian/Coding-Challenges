# The largest two elements in the array can be 1st used and tested.
# The array is 1st ordered then the largest two elements can be popped and added into a new array.
# Then the sum is tested and if the sum is not larger then the largest element in the remainning array can be
# added to array A and the sum recalculated.


def subsetA(arr):
    def subsetA(arr):
        # sort arr
        arr.sort()

        listA = [arr.max(), arr.pop()]

        while sum(listA) < sum(arr):
            listA.append(arr.pop())
        else:
            listA.sort()
            return listA


arr = [6, 5, 3, 2]
subsetA(arr)
