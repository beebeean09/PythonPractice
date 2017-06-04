"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    if head == None:
        return False

    slow = head
    fast = head.next
    while slow != fast:
        if fast == None or fast.next == None:
            return False

        slow = slow.next
        fast = fast.next.next

    return True

#2nd way using a set
def has_cycle2(head):
    current = head
    seen = set()

    while head:
        if current in seen:
            return True
        else:
            seen.add(current)
            if current.next != None:
                current = current.next
            else:
                break

    return False

# 3rd way using dictionary
def has_cycle3(head):
    visited = {}
    while head:
        visited[head] = 1
        if visited.get(head.next, 0) != 0:
            return True
        elif current.next != None:
            current = current.next
        else:
            break

    return False
