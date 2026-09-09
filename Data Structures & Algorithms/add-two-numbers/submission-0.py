# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0, None)
        ans = res
        carry = 0
        while l1 and l2:
            val = l1.val + l2.val + carry
            dummy = ListNode(val % 10, None)
            carry = val // 10
            res.next = dummy
            res = res.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            res.next = l1
            l1 = l1.next
        while l2:
            res.next = l2
            l1 = l2.next

        if carry > 0:
            res.next = ListNode(1, None)
        return ans.next
