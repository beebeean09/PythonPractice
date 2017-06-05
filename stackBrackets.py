def is_matched(expression):
    dic = {'{':'}','[':']','(':')'}
    lst =[]
    for i in expression:
        if i in dic.keys():
            lst.append(dic[i])
        elif len(lst) > 0 and i == lst[-1]:
            lst.pop()
        else:
            return False
    return len(lst) == 0


    pairs_dict = {'}': '{', ']': '[', ')': '('}
    stack = []
    for char in expression:
        if char in pairs_dict.values():
            stack.append(char)
        elif char in pairs_dict:
            if not stack or pairs_dict[char] != stack.pop():
                return False
    return not stack


# long way, only if symmetrical
    # if not expression:
    #     return False
    #
    # par = ['(',')']
    # brack = ['[', ']']
    # curly = ['{', '}']
    #
    # open_seen = []
    # close_seen = []
    #
    # length = len(expression)
    # half = int(length / 2)
    # List = []
    # List.extend(expression)
    # front = List[0:half]
    # back = List[half:length]
    # back.reverse()
    #
    #
    # if len(front) != len(back):
    #     return False
    #
    # for idx in range(len(front)):
    #     if front[idx] in par and back[idx] in par:
    #         pass
    #     elif front[idx] in brack and back[idx] in brack:
    #         pass
    #     elif front[idx] in curly and back[idx] in curly:
    #         pass
    #     else:
    #         return False
    #
    # return True
