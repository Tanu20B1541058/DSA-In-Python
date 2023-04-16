# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):

        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2) :
        dummy=ListNode()
        dd=dummy
        while list1 and list2 :
            if list1.val < list2.val:
                dd.next=list1
                list1=list1.next
            else:
                dd.next=list2
                list2=list2.next
            dd =dd.next
        if list1 :
            dd.next=list1
        else:
            dd.next=list2
        
        return dummy.next
    
######################### Inplace
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2) :
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val > list2.val:
            temp = list1
            list1 = list2
            list2 = temp
        res = list1
        while list1 and list2:
            tmp = None
            while list1 and list1.val <= list2.val:
                tmp = list1
                list1 = list1.next
            tmp.next = list2
            temp = list1
            list1 = list2
            list2 = temp
        return res
            