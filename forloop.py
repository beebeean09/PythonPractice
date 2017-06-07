from math import fabs

def number_needed(a, b):
    letter_idx = [0] * 26
    
    for c in a:
        index = ord(c) - ord('a')
        letter_idx[index] += 1
    
    for c in b:
        index = ord(c) - ord('a')
        letter_idx[index] -= 1
    
    count = 0
    for idx in letter_idx:
        count += fabs(idx)
    
    return int(count)
