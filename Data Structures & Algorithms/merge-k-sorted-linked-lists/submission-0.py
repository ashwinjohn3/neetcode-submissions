from _heapq import heappush, heappop
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        heads = [head for head in lists if head]

        heap = []
        for head in heads: 
            heappush(heap, (head.val, id(head), head))
        
        while heap: 
            val, _, s = heappop(heap)
            current.next = s
            current = current.next

            if current.next:
                heappush(heap, (current.next.val, id(current.next), current.next))
            
        return dummy.next

