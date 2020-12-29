import collections


def anagrams(words: list) -> list:
    result = collections.defaultdict(list)
    for word in words:
        result["".join(sorted(word))].append(word)
    return list(result.values())


if __name__ == "__main__":
    print(anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

