# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head, x: int) :
        if not head or not head.next :
            return head

        print('heh')
        min_dummy = ListNode(0)
        min_head  = min_dummy
        max_dummy = ListNode(0)
        max_head  = max_dummy
        curr = head
        print('heh')

        while curr:
            nxt = curr.next 
            curr.next = None
            if curr.val >= x:
                max_head.next = curr
                max_head = max_head.next
            else:
                min_head.next = curr
                min_head = min_head.next
            curr = nxt

        min_head.next = max_dummy.next

        return min_dummy.next