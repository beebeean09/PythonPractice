"""Write your solution in this file.

You can execute and test your answer by pressing 'Try Answer' in the side panel,
or by running `python test_answer.py <test_case_path>` on the command line.

For example:
    python test_answer.py tests/input_1.json
"""

# Example test case:
# {
#     "boggle_board": [
#         'hel',
#         'owo',
#         'rld'
#     ],
#     "list_path": 'test_input.txt'
# }

def neighbor_pos(position, length):
    # gives me new positions of neighboring letters
    x,y = position
    result = []
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for direction in directions:
        d1,d2 = direction
        k = x + d1
        j = y + d2
        if length - 1 > k > 0 and length - 1 > j > 0:
            result.append((k,j))

    return result

def find_words(boggle_board, list_path):
#     """Implement your solution here.
#
#     Arguments:
#         boggle_board: Array of strings, Representation of a boggle board.
#         list_path: String, Path to a .txt file containing the list of valid words to consider
#
#     Returns:
#         Array of strings, List of valid words found in the given boggle board.
#     """



# Notes:
# - for each letter on grid, all possible letters will be the letter itself and ONLY letters surrounding it
# - ex: 3 by 3 grid with positions [2,2], possible positions ->
#   (+1, +1), (-1, -1), (+1, -1), (-1, + 1), (0, +1), (0, -1), (+1, 0), (-1, 0)
# - half way through this exercise, I realized it might have been easier to use tries/tree to have each letter be a root node and add children nodes if the letters connect to make a word that's included in the dictionary given

    all_words= []
    boggle_words = []
    grid_size = len(boggle_board[0])

    for row_idx in range(grid_size):
        for col_idx in range(grid_size):
            word = ''
            word += boggle_board[row_idx][col_idx]

            neighbors = neighbor_pos((row_idx, col_idx), grid_size)
            for new_pos in neighbors:
                x,y = new_pos
                word += boggle_board[x][y]
                all_words.append(word)


    # open dictionary to check if words are included in the list_path file
    f = open(list_path)
    dictionary = f.readlines()
    new_dictionary = []

    for dict_word in dictionary:
        new_dictionary.append(dict_word.split('\n')[0])

    for word in all_words:
        if word in new_dictionary:
            boggle_words.append(word)


    return boggle_words
