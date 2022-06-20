class Solution:
    def __init__(self):
        self.result = []
        self.prev_elements = []

    def dfs(self, elements):
        if len(elements) == 0:
            self.result.append(self.prev_elements[:])

        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            self.prev_elements.append(e)
            self.dfs(next_elements)
            self.prev_elements.pop()

    def solution(self, nums):
        self.dfs(nums) 
        return self.result


if __name__ == "__main__":
    print(Solution().solution([1, 2, 3]))

