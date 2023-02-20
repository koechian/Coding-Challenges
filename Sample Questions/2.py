# I should be able to traverse a linked list and extract the data in said linked list
# I should then be able to add data to a list and convert it to a string or sth
# then I shouold be able to convert it to decimal using int()

# linked list creation


def getNumber(binary):
    nextval = binary.next
    if nextval is None:
        return binary.data

    data = []
    while nextval is not None:
        data.append(nextval.data)
        nextval = nextval.next

    binStr = "".join(map(str, data))
    return int(binStr, 2)
