class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
        distance = 0

        while distance != n and fast != None:
            fast = fast.next
            distance += 1

        while fast and fast.next != None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next