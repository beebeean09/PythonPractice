def number_needed(a, b):
    count = 0
    a_length = len(a)
    
    a2 = []
    b2 = []
    a2.extend(a)
    b2.extend(b)
    
    for idx in range(a_length):
        if a[idx] in b:
            idx2 = b2.index(a2[idx])
            a2.pop(idx)
            b2.pop(idx2)
        else:
            pass
    
    count = len(a2) + len(b2)
    
    return count


print(number_needed('abbbd', 'abklo'))
