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

# Print a staircase given a num of levels
# length = n + 1
# for idx in range(1,length):
#     spaces = ' ' * (n - idx)
#     hash_tag = '#' * idx
#     print(spaces + hash_tag)

# '     #'
# '    ##'
# '   ###'
# '  ####'
# ' #####'

from math import fabs

def diag_sums(n, arr):
    first_diag = []
    sec_diag = []

    for idx in range(n):
        row = arr[idx]
        first_diag.append(row[idx])

    for idx2 in range(n):
        row = arr[idx2]
        sec_diag.append(row[len(row) - idx2 - 1])

    first_sum = 0
    sec_sum = 0

    for num in first_diag:
        first_sum += num

    for num2 in sec_diag:
        sec_sum += num2

    print(int(fabs(first_sum - sec_sum)))

diag_sums(3, [[1,2,3], [3,2,1], [4,3,2]]) #4
# [1,2,2] - [3,2,4] = |5 - 9| = 4

# Mini-Max Sum, find the sum of all other elements except for current el;
# return the min and max sum
import sys
from functools import reduce

def mini_max_sum(arr):
    max_sum = []
    length = len(arr)
    for num in range(length):
        if arr[:num]:
            front = reduce((lambda x, y: x + y), arr[:num])
        else:
            front = 0
        if arr[num + 1:]:
            back = reduce((lambda x, y: x + y), arr[num + 1:])
        else:
            back = 0

        temp_sum = front + back
        max_sum.append(temp_sum)

    max_sum.sort()
    print(str(max_sum[0]) + ' ' + str(max_sum[-1]))

mini_max_sum([1,2,3,4,5]) # 10 14
