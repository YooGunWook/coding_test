class Solution:
    def __init__(self):
        self.result = []

    def dfs(self, nums, index, path):
        if path not in self.result:
            self.result.append(path)

        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]])

    def solution(self, nums):
        self.dfs(nums, 0, [])
        return self.result


class BookSolution:
    def __init__(self):
        self.result = []

    def dfs(self, index, path):
        self.result.append(path)

        for i in range(index, len(nums)):
            self.dfs(i + 1, path + [nums[i]])

    def solution(self, nums):
        self.dfs(0, [])
        return self.result


if __name__ == "__main__":
    print(Solution().solution([1, 2, 3]))
