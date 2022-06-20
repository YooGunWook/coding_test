class Solution:
    def solution(self, S: str) -> int:
        used = {}
        max_length = 0
        start = 0
        for index, char in enumerate(S):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, index - start + 1)
            used[char] = index
        
        return max_length


if __name__ == "__main__":
    print(Solution().solution("abcabcbb"))

