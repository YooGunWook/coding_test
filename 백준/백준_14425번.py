class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    def add(self, word):
        node = self.root
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.endSymbol] = word

    def search(self, word):
        node = self.root
        for char in word:
            if char in node:
                node = node[char]
            else:
                return False
        if "*" in node.keys():
            return True
        else:
            return False


trie = Trie()
n, m = list(map(int, input().split(" ")))
for _ in range(n):
    trie.add(input())

count = 0
for _ in range(m):
    res = trie.search(input())
    if res == True:
        count += 1
print(count)
# trie.add("안녕하세요")
# trie.add("안녕")
# print(trie.search("안녕"))
# print(trie.root)
