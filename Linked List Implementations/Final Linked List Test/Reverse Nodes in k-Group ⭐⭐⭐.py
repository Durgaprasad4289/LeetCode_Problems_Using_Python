class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k: int):
        if not head.next:
            return head
        curr = head
        length = 0 
        while curr:
            curr = curr.next
            length+=1

        def reverse(head,k):
            if not head or not k:
                return head
            curr = head
            prev = None
            while k:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                k-=1
            return prev,nxt
        dummy = ListNode(0)
        prev  = dummy
        curr  = head
        for i in range(length//k):
            curr_head,next_node = reverse(curr,k)
            prev.next = curr_head
            curr.next = next_node
            prev = curr
            curr = next_node
        return dummy.next