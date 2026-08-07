# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        vals = []
        curr = head

        while curr:
            vals.append(curr.val)
            curr = curr.next

        return vals == vals[::-1]

        