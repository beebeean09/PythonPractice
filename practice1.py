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

# print(bsearch(5, [1,2,3,4,5,8])) #4


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


# print(sort_odds_array([5,3,4,1,2]))
# [1,3,4,5,2]

def SumMultiplier(arr):

    double_sum = 0
    for num in arr:
        double_sum += num

    double_sum = double_sum * 2
    for idx1 in range(len(arr)):
        for idx2 in range(idx1 + 1,len(arr)):
            if arr[idx1] * arr[idx2] > double_sum:
                return True
            else:
                pass

    return False

# print(SumMultiplier([2,2,2,2,4,1])) #False

# Find the word with the most repeated letters.
# Return -1 if no letters repeat in any of the words.

def CountRepLetters(word):
    my_dict = {}
    max_count = 0

    for letter in word:
        if letter in my_dict:
            my_dict[letter] += 1
        else:
            my_dict[letter] = 1

    max_count = max(my_dict.values())
    return max_count


def LetterCount(str):

    max_count = 0
    max_rep_word = ""
    words = str.split(' ')

    for word in words:
        letter_count = CountRepLetters(word)
        if max_count < letter_count and letter_count != 1:
            max_count = letter_count
            max_rep_word = word
        else:
            pass

    if max_rep_word == "":
        return -1

    return max_rep_word

# print(LetterCount('hello my name is vivian')) #hello
# print(LetterCount('my cat is a dog')) #-1

# Return count of digit followed by digit.
def LookSaySequence(num):

    next_num = ''

    num_str = str(num)
    current_num = ''
    current_count = 0

    for idx in range(len(num_str)):
        current_num = num_str[idx] #1 #2
        current_count += 1 #1 #1

        if idx == len(num_str) - 1:
            next_num += (str(current_count) + current_num)
        elif num_str[idx] != num_str[idx + 1]:
            next_num += (str(current_count) + current_num)
            current_count = 0
        else:
            pass

    return next_num

# print(LookSaySequence(1211)) #111221

def NumberEncoding(string):

    my_hash = {}
    result = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for idx in range(27):
        if idx == 26:
            letter = alphabet[25]
            my_hash[letter] = idx
        else:
            letter = alphabet[idx]
            my_hash[letter] = idx + 1

    for el in string:
        if el in alphabet:
            result += str(my_hash[el])
        else:
            result += el


    return result

# print(NumberEncoding("hello 45")) #85121215 45


# Return 1 if brackets do not match. Return 0 if they do match.
def BracketMatcher(str):

    match = False
    bracket = ''
    first = 'default'

    for el in str:
        if el == '(' and first == 'default':
            bracket = el
            first = True
            continue
        elif el == '(' and first == True:
            return 1
        elif el == ')' and first == True:
            return 1
        elif el == ')' and first == False:
            pass


    if first == 'default':
        return 1

    return 0

#print(BracketMatcher('(code)(life)')) #0
#print(BracketMatcher('(r(code)(life)')) #1

# Check if anagrams. Count the number of letters need to delete to make
# anagrams of the two strings
def number_needed(a, b):
    a2  = []
    b2 = []
    a2.extend(a)
    b2.extend(b)
    count = 0

    for el in a2:

        if el in b:
            b_idx = b2.index(el)
            a_idx = a2.index(el)
            del a2[a_idx]
            del b2[b_idx]
        else:
            pass

    count = len(a2) + len(b2)

    return count

print(number_needed('cbl', 'abc')) #4
