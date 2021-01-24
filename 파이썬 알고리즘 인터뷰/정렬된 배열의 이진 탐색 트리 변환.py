# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # list를 무조건 오름차순으로 sort 하고 진행해야 한다.
        if not nums:
            return None

        # 가장 중앙값을 기준으로 계속 쪼개준다.
        mid = len(nums) // 2

        # 재귀 형식으로 계속 쪼갠 것을 기준으로 만들어준다.
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1 :])

        return node