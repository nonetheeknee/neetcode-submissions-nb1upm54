# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tail = head

        while tail and tail.next:
                tail = tail.next.next
                head = head.next
                if tail == head: return True 
        
        return False



        