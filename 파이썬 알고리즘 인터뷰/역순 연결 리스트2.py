class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or m == n:
            return head
        root = start = ListNode(None)

        for _ in range(m - 1):
            start = start.next
        end = start.next

        for _ in range(m, n + 1):
            tmp = start.next
            start = end.next
            end = end.next.next
            start.next.next = tmp

        return root.next

