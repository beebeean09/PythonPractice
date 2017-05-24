def pair_sum(array):
    result = []
    #array = [1,2,3,-1]
    for idx1 in range(0,4):
        for idx2 in range(idx1,4):
            if array[idx1] + array[idx2] == 0:
                result.append([idx1, idx2])

    return result

# print(pair_sum([1,2,3,-1]))

def quicksort(array):
    if len(array) < 2:
        return array

    left = []
    right = []
    length = len(array)
    pivot = array[0]

    for x in array[1:length]:
        if x > pivot:
            right.append(x)
        elif x < pivot:
            left.append(x)
        else:
            pass

    return quicksort(left) + [pivot] + quicksort(right)


# print(quicksort([6,3,2,9,7]))

def unique(array):
    result = []

    for x in array:
        if not x in result:
            result.append(x)

    return result

print unique([1,2,2,3,3,4,3,2,2])
