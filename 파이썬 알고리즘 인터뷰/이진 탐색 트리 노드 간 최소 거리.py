# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.prev = -sys.maxsize
        self.result = sys.maxsize

    def minDiffInBST_stack(self, root: TreeNode) -> int:
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            self.result = min(self.result, node.val - self.prev)
            self.prev = node.val

            node = node.right
        return self.result

    def minDiffInBST(self, root: TreeNode):
        if root.left:
            self.minDiffInBST(root.left)

        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right)

        return self.result