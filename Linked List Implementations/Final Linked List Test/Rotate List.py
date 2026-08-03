from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or not k:
            return head

        length = 1
        curr = head
        while curr.next:
            length+=1
            curr = curr.next

        curr.next = head
        k = k%length
        itr = length-k-1
        curr = head

        for _ in range(itr):
            curr = curr.next

        head = curr.next

        curr.next = None

        return head