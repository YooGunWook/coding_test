class Solution:
    def __init__(self):
        self.result = []

    def dfs(self, elements, start, n, k):
        if k == 0:
            self.result.append(elements[:])
            return

        for i in range(start, n + 1):
            elements.append(i)
            self.dfs(elements, i + 1, n, k - 1)
            elements.pop()

    def solution(self, n, k):
        self.dfs([], 1, n, k)
        return self.result


if __name__ == "__main__":
    print(Solution().solution(5, 3))

