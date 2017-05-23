def pair_sum(array):
    result = []
    #array = [1,2,3,-1]
    for idx1 in range(0,4):
        for idx2 in range(idx1,4):
            if array[idx1] + array[idx2] == 0:
                result.append([idx1, idx2])

    return result

print(pair_sum([1,2,3,-1]))
