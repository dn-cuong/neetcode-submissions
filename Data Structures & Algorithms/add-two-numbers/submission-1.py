class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        res = dummy
        carry = 0

        while l1 and l2:
            val = l1.val + l2.val + carry

            res.next = ListNode(val % 10)
            res = res.next

            carry = val // 10

            l1 = l1.next
            l2 = l2.next

        while l1:
            val = l1.val + carry

            res.next = ListNode(val % 10)
            res = res.next

            carry = val // 10
            l1 = l1.next

        while l2:
            val = l2.val + carry

            res.next = ListNode(val % 10)
            res = res.next

            carry = val // 10
            l2 = l2.next

        if carry:
            res.next = ListNode(carry)

        return dummy.next