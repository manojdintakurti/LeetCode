# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(l1,l2):
            dummy=ListNode(0)
            curr = dummy
            while l1 and l2:
                if l1.val<=l2.val:
                    curr.next=l1
                    l1=l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr=curr.next
            if l1:
                curr.next=l1
            if l2:
                curr.next = l2
            return dummy.next
        if not lists or len(lists)==0:
            return None
        while len(lists) > 1:
            mergedLists = []
            for i in range(0,len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if i+1<len(lists) else None
                mergedLists.append(mergeTwoLists(l1,l2))
            lists=mergedLists
        return lists[0]