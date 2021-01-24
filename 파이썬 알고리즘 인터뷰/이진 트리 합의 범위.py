import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0

        return (
            (root.val if low <= root.val <= high else 0)
            + self.rangeSumBST(root.left, low, high)
            + self.rangeSumBST(root.right, low, high)
        )

    def dfs(self, node: TreeNode, low, high):
        if not node:
            return 0

        if node.val < low:
            return self.dfs(node.right, low, high)
        elif node.val > high:
            return self.dfs(node.left, low, high)

        return (
            node.val + self.dfs(node.left, low, high) + self.dfs(node.right, low, high)
        )

    def rangeSumBST_prune(self, root: TreeNode, low: int, high: int) -> int:
        return self.dfs(root, low, high)

    def rangeSumBST_stack(self, root: TreeNode, low: int, high: int) -> int:
        stack, sum = [root], 0

        # 스택 기반 DFS
        while stack:
            node = stack.pop()
            if node:
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                if low <= node.val <= high:
                    sum += node.val
        return sum

    def rangeSumBST_BFS(self, root: TreeNode, low: int, high: int) -> int:
        queue, sum = collections.deque([root]), 0

        # 스택 기반 DFS
        while queue:
            node = queue.popleft()
            if node:
                if node.val > low:
                    queue.append(node.left)
                if node.val < high:
                    queue.append(node.right)
                if low <= node.val <= high:
                    sum += node.val
        return sum
