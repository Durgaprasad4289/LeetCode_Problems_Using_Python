from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        s = f = head
        prev = None
        while f and f.next:
            prev = s
            s = s.next
            f = f.next.next

        prev.next = None
        
        left = self.sortList(head)
        right = self.sortList(s)

        dummy = ListNode(0)
        curr = dummy

        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        
        if left:
            curr.next = left
        if right:
            curr.next = right

        return dummy.next