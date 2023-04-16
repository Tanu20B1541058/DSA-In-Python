# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        dummy = None
        while head != None:
            nextNode = head.next
            head.next = dummy
            dummy = head
            head = nextNode
        return dummy
        