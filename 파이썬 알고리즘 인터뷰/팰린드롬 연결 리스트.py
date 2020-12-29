import Linked_list
from collections import deque

class Solution:
    def isPalindrome(self, head: Linked_list.ListNode) -> bool:
        q = []

        if not head:
            return True
        print(head)

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True

# 좀 더 빠른 코드
class DequeSolution:
    def isPalindrome(self, head: Linked_list.ListNode) -> bool:
        q = deque()
        
        if not head:
            return True
        
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next
            
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
            
        return True

# 런너 풀이
class RunnerSolution:
    def isPalindrome(self, head: Linked_list.ListNode) -> bool:
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev

if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome([1, 2]))

