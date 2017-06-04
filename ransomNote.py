def ransom_note(magazine, ransom):
    for word in ransom:
        if word not in magazine:
            return False
        else:
            magazine.remove(word)

    return True
