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

# print unique([1,2,2,3,3,4,3,2,2])

def is_substring(mainStr, str1):
    if str1 in mainStr:
        return True

    return False

# print(is_substring('hello', 'el'))

def is_prime(number):
    if number < 2:
        return False

    for x in range(2,number):
        if number % x == 0:
            return False

    return True

# print(is_prime(5))
# print(is_prime(2))
# print(is_prime(9))
# print(is_prime(3))


# You are working on a phone book application. Since users often enter their phone numbers using different formats, such as (650) 555-1234 or 650 555 1234, you would like to write a function to normalize these numbers to a common format,  650-555-1234.
#
# Implement the Java function standardizePhoneNumber, which converts the input phone numbers into the standard format  or returns an empty string if the input phone number is invalid.
#
# (650) 555-1234 650-555-1234
# 65.0555.1234 650-555-1234
# 65/05/5512/34 650-555-1234
# (650) 555-1234 x111 is invalid
# (650) 555-123 is invalid

def phone_book(number):
    integers = ['1','2','3','4','5','6','7','8','9','0']
    phone_num = ''

    for x in number:
        if len(phone_num) == 3 and x in integers:
            phone_num += '-' + x
        elif len(phone_num) == 7 and x in integers:
            phone_num += '-' + x
        elif x in integers:
            phone_num += x
        else:
            pass

    if len(phone_num) == 12:
        return phone_num
    else:
        return False
#
# print(phone_book('(650) 555-1234)'))
# print(phone_book('(650) 555-x1234 234)'))
# print(phone_book('(650) 555-x)'))
# print(phone_book('6475667384'))

def fizz_buzz(array):
    result = []

    for x in array:
        if (x % 3 == 0 and x % 5 != 0) or (x % 3 != 0 and x % 5 == 0):
            result.append(x)
        else:
            pass

    return result

# print(fizz_buzz([12, 15, 3, 10, 2, 30, 7]))

# def titleize(title):
#     not_these =['a', 'the', 'over', 'of']
#     words = title.split(' ')
#     result = []
#
#     for word in words[0:]:
#         if word in not_these:
#             result.append(word)
#         else:
#             result.append(word.capitalize)
#
#     return result.join(' ')
#
#
# print(titleize('hello my name is vivian and I like to go over the rainbow of the sky.'))

def bsearch(target, list_arr):
    if len(list_arr) == 0:
        return -1

    result = 0

    middle_idx = int(len(list_arr) / 2)
    # print(middle_idx)
    if list_arr[middle_idx] == target:
        # print(list_arr[middle_idx])
        # print(middle_idx)
        return middle_idx
    elif list_arr[middle_idx] > target:
        left = list_arr[0:middle_idx]
        return bsearch(target, left)
    elif list_arr[middle_idx] < target:
        # print(list_arr[middle_idx + 1: len(list_arr)])
        subs_list = bsearch(target, list_arr[middle_idx + 1: len(list_arr)])
        if subs_list == -1:
            return -1
        else:
            result = subs_list + middle_idx + 1

    return result

print(bsearch(5, [1,2,3,4,5,8])) #4


# You have an array of numbers.
# Your task is to sort ascending odd numbers but even numbers must be on their places.
#
# Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.
#
# Example
#
# sortArray([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]

def sort_odds_array(source_array):

    odd_nums = []
    indices = []

    for idx,num in enumerate(source_array):
        if num % 2 != 0:
            odd_nums.append(num)
            indices.append(idx)
        else:
            pass

    odd_nums.sort()
    idx = 0
    for odd_num in odd_nums:
        source_array[indices[idx]] = odd_num
        idx += 1

    return source_array


print(sort_odds_array([5,3,4,1,2]))
# [1,3,4,5,2]
