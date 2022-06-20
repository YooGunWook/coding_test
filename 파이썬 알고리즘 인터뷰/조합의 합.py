class Solution:
    def __init__(self):
        self.result = []

    def dfs(self, csum, index, path, candidates):
        if csum < 0:
            return
        if csum == 0:
            self.result.append(path)
            return
        for i in range(index, len(candidates)):
            self.dfs(csum - candidates[i], i, path + [candidates[i]], candidates)

    def solution(self, candidates: list, target: int) -> list:
        self.dfs(target, 0, [], candidates)
        return self.result


if __name__ == "__main__":
    print(Solution().solution([2, 3, 5], 8))

