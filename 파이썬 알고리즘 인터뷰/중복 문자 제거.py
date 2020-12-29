class Solution:
    def recursive_solution(self, s: str) -> str:
        for char in sorted(set(s)):
            suffix = s[s.index(char) :]
            if set(s) == set(suffix):
                return char + self.recursive_solution(suffix.replace(char, ""))
        return ""

    def stack_solution(self, s: str) -> str:
        import collections

        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return "".join(stack)


if __name__ == "__main__":
    print(Solution().recursive_solution("cbacdcbc"))
    print(Solution().stack_solution("cbacdcbc"))
    print("c" > "b")

