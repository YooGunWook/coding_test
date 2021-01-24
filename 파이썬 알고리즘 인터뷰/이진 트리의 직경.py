import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.longest = 0

    # dfs 구현
    def dfs(self, node: TreeNode):
        if not node:
            return -1
        # 왼쪽과 오른쪽의 각 리프 노드까지 탐색
        left = self.dfs(node.left)
        right = self.dfs(node.right)

        # 가장 긴 부분 탐색
        self.longest = max(self.longest, left + right + 2)
        return max(left, right) + 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.longest
