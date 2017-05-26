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


def parse_time(str_time):
    # '12:00:00'




f = open('sample.txt')
lines = f.readlines()
time_hash = {}

for line in lines:
    time_status = line.split('::')
    status = (time_status[1]).split('\n')[0]
    # print(status)
    time = (time_status[0]).split('-')[1]
    time = time.split(')')[0]
    # print(time)
    if status in time_hash:
        time_hash[status] -= parse_time(time))
    else:
        time_hash[status] = time

print(time_hash)
