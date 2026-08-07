"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        oldtonew = {}
        curr = head

        while curr:
            oldtonew[curr] = Node(curr.val)
            curr = curr.next
        curr = head

        while curr:
            copy = oldtonew[curr]
            copy.next = oldtonew.get(curr.next)
            copy.random = oldtonew.get(curr.random)
            curr = curr.next
        
        return oldtonew[head]

        