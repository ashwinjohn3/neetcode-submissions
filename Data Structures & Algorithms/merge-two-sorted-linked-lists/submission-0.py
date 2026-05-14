# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        head1 = list1
        head2 = list2
        dummy = new_node = ListNode()
        while head1 and head2: 
            if head1.val < head2.val:
                new_node.next = head1
                head1 = head1.next
            else: 
                new_node.next = head2
                head2 = head2.next
            new_node = new_node.next
        new_node.next = head1 or head2
        return dummy.next




                
        