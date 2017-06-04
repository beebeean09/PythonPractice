"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    print(head)
    if head.data == None:
        return False
    elif head.next.data == None:
        return False

    current = head
    next_current = head.next
    after_next_current = current.next
    while next_current.data != None:
        if after_current == current:
            return False
        else:
            current = next_current
    
