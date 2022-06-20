class Solution:
    def __init__(self):
        self.result = []

    def dfs(self, digits, index, path):

        phone_digits = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        if len(path) == len(digits):
            self.result.append(path)
            return

        for i_index in range(index, len(digits)):
            for digit in phone_digits[digits[i_index]]:
                self.dfs(digits, i_index + 1, path + digit)

    def solution(self, digits):
        if not digits:
            return []

        self.dfs(digits, 0, "")

        return self.result


if __name__ == "__main__":
    print(Solution().solution("23"))

