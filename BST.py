""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

# def checkBST(root):
#     "print(root.right.data)"
#     "print(root.left.data)"
#     "print(root.data)"
#
#     if root.left == None or root.right == None:
#         return 'Yes'
#     elif root.data < root.left.data or root.data > root.right.data:
#         return 'No'
#     elif root.data > root.left.data:
#         return checkBST(root.left)
#     elif root.data < root.right.data:
#         return checkBST(root.right)

def checkBST(root):
    toList = in_order(root)
    print(toList)
    for index in range(1, len(toList)):
        if toList[index - 1] >= toList[index]:
            return False
    return True


def in_order(root, lst=[]):
    if root:
        in_order(root.left)
        lst.append(root.data)
        in_order(root.right)
    return lst

root = 2
tree = 1 2 3 4 5 6 7
# returns Yes (It is a BST)
        '4'
      '/   \'
    '2       6'
  '/   \   /   \'
  '1    3 5     7'
