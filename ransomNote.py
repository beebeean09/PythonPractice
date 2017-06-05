def ransom_note(magazine, ransom):
# With list (slower)
    for word in ransom:
        if word not in magazine:
            return False
        else:
            magazine.remove(word)

    return True

# With dictionary (faster)
    # ndict = {}
    # for k in magazine:
    #     if k in ndict:
    #         ndict[k] += 1
    #     else:
    #         ndict[k] = 1
    # count = 0
    # for item in ransom:
    #     if item in ndict:
    #         value = ndict[item]
    #         if value > 0:
    #             ndict[item] -= 1
    #             count += 1
    #         else:
    #             break
    #     else:
    #         break
    # return len(ransom) == count
