import collections
import re


def check_frequent_word(paragraph: str, banned: list) -> str:
    p = re.compile(r"[^\w]")
    new_para = [
        word for word in p.sub(" ", paragraph).lower().split() if word not in banned
    ]
    result = collections.Counter(new_para)
    return result.most_common(1)[0][0]


if __name__ == "__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"
    banned = ["hit"]
    print(check_frequent_word(paragraph, banned))

