class Solution:
    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "1":
            return
        grid[i][j] = "0"

        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

    def solution(self, grid) -> int:
        if not grid:
            return 0

        count = 0
        for i_index in range(len(grid)):
            for j_index in range(len(grid)):
                if grid[i_index][j_index] == "1":
                    self.dfs(grid, i_index, j_index)
                    count += 1
        return count


if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    print(Solution().solution(grid))

