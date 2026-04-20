# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        node1 = head
        node2 = node1.next
        node1.next = None

        while node2:
            temp = node2.next
            node2.next = node1
            node1 = node2
            node2 = temp

        return node1
