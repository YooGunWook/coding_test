import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_ids = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def is_panlidrome(word: str):
        return word[::] == word[::-1]

    def insert(self, index, word) -> None:
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_panlidrome(word[0 : len(word) - i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
        node.word_id = index

    def search(self, index, word) -> list:
        result = []
        node = self.node

        while word:
            # 판별 로직 3
            if node.word_id >= 0:
                if self.is_panlidrome(word):
                    result.append([index, node.word_id])
            if not word[0] in node.children:
                return False
            node = node.children[word[0]]
            word = word[1:]

        # 판별 로직 1
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])

        # 판별 로직 3
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])

        return result


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        result = []
        queue = collections.deque(words)
        for i in range(len(queue)):
            word = queue.popleft()
            for check in queue:
                palindrome_check = word + check
                if palindrome_check == palindrome_check[::-1]:
                    result.append([i, words.index(check)])
            queue.append(word)
        return result

    def PalindromeTrie(self, words):
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(i, word)

        result = []
        for i, word in enumerate(words):
            result.extend(trie.search(i, word))

        return result
