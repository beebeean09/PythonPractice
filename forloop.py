def neighbor_pos(position):
    # gives me new positions of neighboring letters
    x,y = position
    result = []
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    for direction in directions:
        d1,d2 = direction
        k = x + d1
        j = y + d2
        if k > 0 and j > 0:
            result.append([k,j])

    return result

print(neighbor_pos((1,1)))
