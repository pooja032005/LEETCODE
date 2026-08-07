# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        visited =set()
        current = head

        while current:
            if current in  visited :
                return current

            visited.add(current)
            current = current.next 

        return None
