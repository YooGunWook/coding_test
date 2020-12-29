class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        string_book = {")": "(", "}": "{", "]": "["}
        for i_string in s:
            if i_string not in string_book:
                stack.append(i_string)
                print(stack)
            elif not stack or string_book[i_string] != stack.pop():
                return False
        return len(stack) == 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid("([)]"))
