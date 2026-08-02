from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0,head)
        curr = dummy
        curr_sum = 0
        nodes = {}

        while curr:
            curr_sum+=curr.val
            nodes[curr_sum] = curr
            curr = curr.next

        curr = dummy
        curr_sum = 0

        while curr:
            curr_sum+=curr.val
            curr.next = nodes[curr_sum].next
            curr = curr.next

        return dummy.next