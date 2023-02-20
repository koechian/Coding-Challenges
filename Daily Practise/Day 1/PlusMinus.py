# get count of the non 0 elements
from fractions import Fraction


def ratio(arr):
    elms = {"negatives": 0, "positives": 0, "zero": 0}
    for item in arr:
        if item > 0:
            elms["positives"] = elms["positives"] + 1
        elif item == 0:
            elms["zero"] = elms["zero"] + 1
        elif item < 0:
            elms["negatives"] = elms["negatives"] + 1

    print("{0:.6f}".format(elms["positives"] / len(arr)))
    print("{0:.6f}".format(elms["negatives"] / len(arr)))
    print("{0:.6f}".format(elms["zero"] / len(arr)))


arr = [1, 1, 0, -1, -1]

ratio(arr)
