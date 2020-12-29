# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev
    
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_reverse = self.reverseList(l1)
        l2_reverse = self.reverseList(l2)
        l1_value_str = ''
        l2_value_str = ''
        prev: ListNode = None
        
        while l1_reverse:
            l1_value = l1_reverse.val
            l1_value_str += str(l1_value)
            l1_reverse = l1_reverse.next
            
        while l2_reverse:
            l2_value = l2_reverse.val
            l2_value_str += str(l2_value)
            l2_reverse = l2_reverse.next
        
        sum_value = list(str(int(l1_value_str) + int(l2_value_str)))
        for r in sum_value:
            node = ListNode(r)
            node.next = prev
            prev = node
            
        return node
        
class OtherSolution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)
        
        carry = 0
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next
