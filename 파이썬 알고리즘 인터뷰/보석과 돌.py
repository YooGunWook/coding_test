import collections


class Solution:
    def solution(self, J: str, S: str) -> int:
        hashmap = collections.Counter(S)
        result = 0
        for j in J:
            if j in hashmap:
                result += hashmap[j]
        return result

    def one_line_solution(self, J: str, S: str) -> int:
        return sum(s in J for s in S)


if __name__ == "__main__":
    S = "aAAbbbb"
    J = "aA"
    print(Solution().solution(J, S))
    print(Solution().one_line_solution(J, S))

