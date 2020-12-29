class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd = head
        even = head.next
        even_head = head.next

        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even = even.next.next
            even = even.next

        odd.next = even_head
        return head