class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def findLength(node):
            count = 0
            while node:
                count += 1
                node = node.next
            return count
        
        length = findLength(head)
        if n == length:
            return head.next  # remove the head

        temp = head
        for _ in range(length - n - 1):
            temp = temp.next

        temp.next = temp.next.next
        return head
