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

    def startswith(self, prefix):
        node = self.root
        for char in prefix:
            if char in node:
                node = node[char]

        return len(node)


t = int(input())
for i in range(t):
    n = int(input())
    num_list = []
    for _ in range(n):
        num_list.append(input())
    trie = Trie()
    for idx in range(len(num_list)):
        trie.add(num_list[idx])
    for idx in range(len(num_list)):
        res = trie.startswith(num_list[idx])
        if res >= 2:
            print("NO")
            break
    if res >= 2:
        continue
    else:
        print("YES")
