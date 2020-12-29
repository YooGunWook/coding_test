import collections


class Solution:
    def check_temperature(self, T: list) -> list:
        stack = []
        answer = [0] * len(T)
        for i, cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)

        return answer


if __name__ == "__main__":
    print(Solution().check_temperature([73, 74, 75, 71, 69, 72, 76, 73]))

