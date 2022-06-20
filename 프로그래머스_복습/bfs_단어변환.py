from collections import deque
import copy


def solution(begin, target, words):
    queue = deque([([begin], 0)])
    answer = 0
    while queue:
        word_list, count = queue.popleft()
        now_word = word_list[-1]
        if now_word == target:
            break
        for word in words:
            if word in word_list:
                continue
            tmp_count = 0
            for i in range(len(now_word)):
                if now_word[i] != word[i]:
                    tmp_count += 1
            if tmp_count == 1:
                tmp_word_list = copy.deepcopy(word_list)
                tmp_count = copy.deepcopy(count)
                tmp_word_list.append(word)
                tmp_count += 1
                queue.append((tmp_word_list, tmp_count))

    return count


if __name__ == "__main__":
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(solution(begin, target, words))
