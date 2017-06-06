def array_sum(arr):
    #By using reduce; imported function
    from functools import reduce
    product = reduce((lambda x, y: x + y), arr)
    print(product)

    # By iterating
    # sum = 0
    # for num in arr:
    #     sum += num
    # print(sum)

array_sum([1,2,3,4])


def solve_triplets(a0, a1, a2, b0, b1, b2):
    a = [a0, a1, a2]
    b = [b0, b1, b2]
    alice = 0
    bob = 0

    for idx in range(3):
        if a[idx] > b[idx]:
            alice += 1
        elif a[idx] < b[idx]:
            bob += 1
        else:
            pass

    print(str(alice) + ' ' + str(bob))

solve_triplets(3,1,2,1,5,2)

def lonely_integer(a):
    my_hash = {}
    for num in a:
        if num in my_hash:
            my_hash[num] += 1
        else:
            my_hash[num] = 1

    for el in my_hash:
        if my_hash[el] == 1:
            return el
        else:
            pass


print(lonely_integer([1,3,4,6,3,1,4]))
