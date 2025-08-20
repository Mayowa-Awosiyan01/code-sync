# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        vals = []
        if len(lists) ==0:
            return None

        for link in lists:
            if link is not None:
                while link:
                    heapq.heappush(vals,link.val)
                    link=link.next
        
        if vals:
            head = ListNode()
            head = ListNode(heapq.heappop(vals))
            tmp=head
            while vals:
                tmp.next = ListNode(heapq.heappop(vals))
                tmp=tmp.next

        else:
            return None
        
        return head