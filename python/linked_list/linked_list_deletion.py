class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        #while head and head.next==head.val:
        #    head = head.next
        curr = head
        while curr:
            if curr.next and curr.next.val==curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
