# https://leetcode.com/problems/swap-nodes-in-pairs/

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution_1:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        
        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
        
        return head
    
class Solution_2:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode(None)
        prev.next = head
        
        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head
            
            prev.next = b
            
            head = head.next
            prev = prev.next.next
        return root.next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head